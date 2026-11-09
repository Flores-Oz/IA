from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "app_data"

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
 id INTEGER PRIMARY KEY, sha TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
 stored_path TEXT NOT NULL, page_count INTEGER NOT NULL, extracted_pages INTEGER NOT NULL,
 status TEXT NOT NULL, warnings TEXT NOT NULL DEFAULT '[]',
 created TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);
CREATE TABLE IF NOT EXISTS pages (
 id INTEGER PRIMARY KEY, document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
 number INTEGER NOT NULL, text TEXT NOT NULL, heading TEXT NOT NULL, method TEXT NOT NULL,
 warning TEXT NOT NULL DEFAULT '', UNIQUE(document_id, number)
);
CREATE TABLE IF NOT EXISTS topics (
 id INTEGER PRIMARY KEY, title TEXT NOT NULL, normalized TEXT NOT NULL UNIQUE,
 understood INTEGER NOT NULL DEFAULT 0, difficulty INTEGER NOT NULL DEFAULT 2,
 fundamental INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS topic_pages (
 topic_id INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
 page_id INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
 PRIMARY KEY(topic_id,page_id)
);
CREATE TABLE IF NOT EXISTS topic_links (
 prerequisite_id INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
 dependent_id INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
 reason TEXT NOT NULL, PRIMARY KEY(prerequisite_id,dependent_id),
 CHECK(prerequisite_id != dependent_id)
);
CREATE TABLE IF NOT EXISTS guides (
 id INTEGER PRIMARY KEY, topic_id INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
 level TEXT NOT NULL, simple INTEGER NOT NULL, source_hash TEXT NOT NULL,
 model TEXT NOT NULL, content TEXT NOT NULL,
 UNIQUE(topic_id,level,simple)
);
CREATE TABLE IF NOT EXISTS questions (
 id INTEGER PRIMARY KEY, topic_id INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
 kind TEXT NOT NULL, difficulty TEXT NOT NULL, prompt TEXT NOT NULL,
 options TEXT NOT NULL DEFAULT '[]', answer TEXT NOT NULL, explanation TEXT NOT NULL,
 refs TEXT NOT NULL, rubric TEXT NOT NULL, generator TEXT NOT NULL,
 signature TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS exams (
 id INTEGER PRIMARY KEY, status TEXT NOT NULL DEFAULT 'active',
 started REAL NOT NULL, deadline REAL NOT NULL, question_ids TEXT NOT NULL,
 state TEXT NOT NULL, finished REAL, settings TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS attempts (
 id INTEGER PRIMARY KEY, question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
 response TEXT NOT NULL, score REAL CHECK(score IS NULL OR (score >= 0 AND score <= 1)),
 graded_by TEXT NOT NULL, feedback TEXT NOT NULL, exam_id INTEGER REFERENCES exams(id),
 created TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);
CREATE UNIQUE INDEX IF NOT EXISTS one_active_exam ON exams(status) WHERE status='active';
CREATE UNIQUE INDEX IF NOT EXISTS exam_question_attempt ON attempts(exam_id,question_id)
 WHERE exam_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS attempt_question ON attempts(question_id,id);
CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
PRAGMA user_version=1;
"""


class Database:
    def __init__(self, data_dir: Path = DEFAULT_DATA):
        self.data_dir = Path(data_dir).resolve()
        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "documents").mkdir(exist_ok=True)
        self.path = self.data_dir / "study.sqlite3"
        with self.connect() as conn:
            conn.executescript(SCHEMA)

    @contextmanager
    def connect(self):
        conn = sqlite3.connect(self.path, timeout=30)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys=ON")
        try:
            with conn:
                yield conn
        finally:
            conn.close()

    def all(self, sql: str, params=()) -> list[dict]:
        with self.connect() as conn:
            return [dict(row) for row in conn.execute(sql, params).fetchall()]

    def one(self, sql: str, params=()) -> dict | None:
        rows = self.all(sql, params)
        return rows[0] if rows else None

    def execute(self, sql: str, params=()) -> int:
        with self.connect() as conn:
            cur = conn.execute(sql, params)
            return cur.lastrowid or 0

    def get(self, key: str, default: Any = None) -> Any:
        row = self.one("SELECT value FROM settings WHERE key=?", (key,))
        return json.loads(row["value"]) if row else default

    def set(self, key: str, value: Any):
        self.execute("INSERT INTO settings(key,value) VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                     (key, json.dumps(value, ensure_ascii=False)))

    def topics(self) -> list[dict]:
        return self.all("""SELECT t.*, COUNT(DISTINCT tp.page_id) page_count,
            COUNT(DISTINCT p.document_id) document_count FROM topics t
            LEFT JOIN topic_pages tp ON tp.topic_id=t.id
            LEFT JOIN pages p ON p.id=tp.page_id GROUP BY t.id ORDER BY t.id""")

    def sources(self, topic_id: int) -> list[dict]:
        return self.all("""SELECT p.*,d.name document_name,d.stored_path,d.sha
            FROM pages p JOIN topic_pages tp ON tp.page_id=p.id
            JOIN documents d ON p.document_id=d.id WHERE tp.topic_id=?
            ORDER BY d.id,p.number""", (topic_id,))

    def question(self, question_id: int) -> dict | None:
        row = self.one("SELECT q.*,t.title topic_title FROM questions q JOIN topics t ON t.id=q.topic_id WHERE q.id=?",
                       (question_id,))
        if row:
            for key in ("options", "refs", "rubric"):
                row[key] = json.loads(row[key])
        return row

    def merge_topics(self, source: int, target: int):
        if source == target:
            raise ValueError("Selecciona dos temas diferentes.")
        with self.connect() as conn:
            if len(conn.execute("SELECT id FROM topics WHERE id IN (?,?)", (source, target)).fetchall()) != 2:
                raise ValueError("No se encontraron ambos temas.")
            conn.execute("INSERT OR IGNORE INTO topic_pages SELECT ?,page_id FROM topic_pages WHERE topic_id=?", (target, source))
            conn.execute("UPDATE questions SET topic_id=? WHERE topic_id=?", (target, source))
            conn.execute("INSERT OR IGNORE INTO topic_links SELECT ?,dependent_id,reason FROM topic_links WHERE prerequisite_id=? AND dependent_id!=?", (target, source, target))
            conn.execute("INSERT OR IGNORE INTO topic_links SELECT prerequisite_id,?,reason FROM topic_links WHERE dependent_id=? AND prerequisite_id!=?", (target, source, target))
            conn.execute("UPDATE topics SET fundamental=MAX(fundamental,(SELECT fundamental FROM topics WHERE id=?)) WHERE id=?", (source, target))
            conn.execute("DELETE FROM guides WHERE topic_id=?", (target,))
            conn.execute("DELETE FROM topics WHERE id=?", (source,))
