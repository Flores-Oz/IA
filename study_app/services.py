from __future__ import annotations

import csv
import io
import json
import math
import random
import time

from .content import OBJECTIVE
from .database import Database


def has_response(value) -> bool:
    return value is not None and str(value).strip() != ""


def grade(question: dict, response) -> tuple[float | None, str, str]:
    if not has_response(response):
        return 0.0, "sin respuesta", "No se registró ninguna respuesta. Revisa la respuesta modelo y vuelve a intentarlo."
    if question["kind"] in OBJECTIVE:
        correct = str(response) == question["answer"]
        return float(correct), "objetiva", ("Respuesta correcta. " if correct else "Respuesta incorrecta. ") + question["explanation"]
    return None, "pendiente", "Compara tu respuesta con el modelo y aplica la rúbrica. No se ha calculado una nota automática."


def schedule_retry(db: Database, question_id: int, attempt_id: int):
    q = db.question(question_id)
    queue = db.get("retry_queue", [])
    queue = [r for r in queue if r["topic_id"] != q["topic_id"]]
    queue.append({"topic_id": q["topic_id"], "avoid": question_id, "after": attempt_id + 2})
    db.set("retry_queue", queue[-60:])


def record_attempt(db: Database, question_id: int, response) -> int:
    q = db.question(question_id)
    if not q:
        raise ValueError("No se encontró la pregunta.")
    score, by, feedback = grade(q, response)
    attempt_id = db.execute("INSERT INTO attempts(question_id,response,score,graded_by,feedback) VALUES (?,?,?,?,?)",
                            (question_id, json.dumps(response, ensure_ascii=False), score, by, feedback))
    if score is not None and score < .7:
        schedule_retry(db, question_id, attempt_id)
    return attempt_id


def self_assess(db: Database, attempt_id: int, score: float):
    if score not in {0.0, .5, 1.0}:
        raise ValueError("Valor de autoevaluación inválido.")
    attempt = db.one("SELECT * FROM attempts WHERE id=?", (attempt_id,))
    if not attempt or attempt["graded_by"] != "pendiente":
        raise ValueError("Esta respuesta ya fue calificada o no requiere autoevaluación.")
    db.execute("UPDATE attempts SET score=?,graded_by='autoevaluación',feedback=? WHERE id=? AND score IS NULL",
               (score, "Autoevaluación del estudiante con respuesta modelo y rúbrica.", attempt_id))
    if score < .7:
        schedule_retry(db, attempt["question_id"], attempt_id)


def topic_stats(db: Database) -> dict[int, dict]:
    result = {}
    for topic in db.topics():
        rows = db.all("""SELECT a.*,q.topic_id FROM attempts a JOIN questions q ON q.id=a.question_id
            WHERE q.topic_id=? AND a.score IS NOT NULL ORDER BY a.id DESC""", (topic["id"],))
        recent = rows[:10]
        unique = len({a["question_id"] for a in recent})
        accuracy = sum(a["score"] for a in recent) / len(recent) if recent else None
        streak = 0
        for row in rows:
            if row["score"] < .8:
                break
            streak += 1
        mastered = len(recent) >= 4 and unique >= 3 and streak >= 3 and accuracy >= .8
        state = "Dominio orientativo" if mastered else ("En práctica" if rows else ("Leído / comprendido" if topic["understood"] else "Sin comprobar"))
        dependents = db.one("SELECT COUNT(*) n FROM topic_links WHERE prerequisite_id=?", (topic["id"],))["n"]
        weakness = (1 - accuracy) if accuracy is not None else .6
        priority = 1 + weakness * 4 + topic["difficulty"] * .4 + min(topic["document_count"], 5) * .4
        priority += int(topic["fundamental"]) * 2 + min(dependents, 5) * .5
        if mastered:
            priority *= .45
        result[topic["id"]] = {**topic, "attempts": len(rows), "accuracy": accuracy, "mastered": mastered,
                                "state": state, "unique": unique, "streak": streak, "priority": priority,
                                "self_assessed": sum(a["graded_by"] == "autoevaluación" for a in rows)}
    return result


def weak_questions(db: Database, unresolved=True) -> list[dict]:
    # Latest scored attempt per question determines whether it remains unresolved.
    rows = db.all("""SELECT a.*,q.prompt,q.topic_id,q.kind,q.explanation,t.title topic_title
        FROM attempts a JOIN questions q ON q.id=a.question_id JOIN topics t ON t.id=q.topic_id
        WHERE a.score < .7 ORDER BY a.id DESC""")
    if not unresolved:
        return rows
    seen, result = set(), []
    for row in rows:
        if row["question_id"] in seen:
            continue
        seen.add(row["question_id"])
        latest = db.one("SELECT score FROM attempts WHERE question_id=? AND score IS NOT NULL ORDER BY id DESC LIMIT 1", (row["question_id"],))
        if latest and latest["score"] < .7:
            result.append(row)
    return result


def select_practice(db: Database, topic_ids=None, kinds=None, difficulty=None, exclude=None) -> dict | None:
    candidates = db.all("SELECT id,topic_id,kind,difficulty FROM questions")
    candidates = [q for q in candidates if (topic_ids is None or q["topic_id"] in topic_ids)
                  and (not kinds or q["kind"] in kinds) and (not difficulty or q["difficulty"] == difficulty)]
    if not candidates:
        return None
    alternatives = [q for q in candidates if q["id"] != exclude]
    if alternatives:
        candidates = alternatives
    last_id = db.one("SELECT COALESCE(MAX(id),0) n FROM attempts")["n"]
    queue = db.get("retry_queue", [])
    for retry in queue:
        due = [q for q in candidates if q["topic_id"] == retry["topic_id"] and q["id"] != retry["avoid"]]
        if retry["after"] <= last_id and due:
            selected = random.choice(due)
            db.set("retry_queue", [r for r in queue if r != retry])
            return db.question(selected["id"])
    stats = topic_stats(db)
    def priority(q):
        latest = db.one("SELECT id,score FROM attempts WHERE question_id=? ORDER BY id DESC LIMIT 1", (q["id"],))
        p = stats[q["topic_id"]]["priority"]
        if latest:
            p += 1 if latest["score"] is not None and latest["score"] < .7 else -1
            p -= max(0, 3 - (last_id - latest["id"])) * 2
        else:
            p += 3
        return p + random.random()
    selected = max(candidates, key=priority)
    return db.question(selected["id"])


def exam_row(db: Database, exam_id: int) -> dict | None:
    row = db.one("SELECT * FROM exams WHERE id=?", (exam_id,))
    if row:
        for field in ("question_ids", "state", "settings"):
            row[field] = json.loads(row[field])
    return row


def create_exam(db: Database, count: int, topic_ids: list[int], kinds: list[str], difficulty=None,
                minutes=60, randomized=True) -> int:
    if not topic_ids or not kinds or count < 1 or minutes <= 0:
        raise ValueError("Selecciona temas, tipos, duración y una cantidad positiva.")
    if db.one("SELECT id FROM exams WHERE status='active'"):
        raise ValueError("Ya existe un simulacro activo. Finalízalo antes de crear otro.")
    candidates = db.all("SELECT id,topic_id,kind,difficulty FROM questions ORDER BY id")
    candidates = [q for q in candidates if q["topic_id"] in topic_ids and q["kind"] in kinds
                  and (not difficulty or q["difficulty"] == difficulty)]
    if len(candidates) < count:
        raise ValueError(f"Hay {len(candidates)} preguntas que cumplen los filtros. Reduce la cantidad o genera más preguntas.")
    if randomized:
        candidates = random.sample(candidates, count)
    else:
        stats = topic_stats(db)
        candidates = sorted(candidates, key=lambda q: (-stats[q["topic_id"]]["priority"], q["id"]))[:count]
    now = time.time()
    return db.execute("INSERT INTO exams(started,deadline,question_ids,state,settings) VALUES (?,?,?,?,?)",
        (now, now + minutes * 60, json.dumps([q["id"] for q in candidates]),
         json.dumps({"answers": {}, "flags": [], "index": 0}),
         json.dumps({"topics": topic_ids, "kinds": kinds, "difficulty": difficulty, "minutes": minutes, "randomized": randomized})))


def update_exam(db: Database, exam_id: int, *, question_id=None, response=None, index=None, flag=None):
    with db.connect() as conn:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM exams WHERE id=?", (exam_id,)).fetchone()
        if not row or row["status"] != "active" or time.time() >= row["deadline"]:
            raise ValueError("El simulacro ya finalizó o se agotó el tiempo. No se guardaron cambios fuera de plazo.")
        state = json.loads(row["state"])
        ids = json.loads(row["question_ids"])
        if question_id is not None and question_id not in ids:
            raise ValueError("La pregunta no pertenece al simulacro.")
        if question_id is not None and flag is None:
            state["answers"][str(question_id)] = response
        if flag is not None and question_id is not None:
            flags = set(state["flags"])
            flags.add(question_id) if flag else flags.discard(question_id)
            state["flags"] = sorted(flags)
        if index is not None:
            if not 0 <= index < len(ids):
                raise ValueError("Posición inválida.")
            state["index"] = index
        conn.execute("UPDATE exams SET state=? WHERE id=? AND status='active'", (json.dumps(state, ensure_ascii=False), exam_id))


def finish_exam(db: Database, exam_id: int):
    # One transaction: repeated timeout/finish events cannot create extra attempts.
    with db.connect() as conn:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT * FROM exams WHERE id=?", (exam_id,)).fetchone()
        if not row or row["status"] != "active":
            return
        state = json.loads(row["state"])
        for qid in json.loads(row["question_ids"]):
            question = dict(conn.execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone())
            response = state["answers"].get(str(qid))
            score, by, feedback = grade(question, response)
            conn.execute("INSERT OR IGNORE INTO attempts(question_id,response,score,graded_by,feedback,exam_id) VALUES (?,?,?,?,?,?)",
                         (qid, json.dumps(response, ensure_ascii=False), score, by, feedback, exam_id))
        conn.execute("UPDATE exams SET status='finished',finished=? WHERE id=?", (time.time(), exam_id))


def exam_result(db: Database, exam_id: int) -> dict:
    rows = db.all("""SELECT a.*,q.kind,q.topic_id,t.title topic_title FROM attempts a JOIN questions q ON q.id=a.question_id
        JOIN topics t ON t.id=q.topic_id WHERE a.exam_id=? ORDER BY a.id""", (exam_id,))
    objective = [r for r in rows if r["kind"] in OBJECTIVE]
    scored = [r for r in rows if r["score"] is not None]
    pending = len(rows) - len(scored)
    return {"rows": rows, "objective_percent": 100 * sum(r["score"] or 0 for r in objective) / len(objective) if objective else None,
            "objective_count": len(objective), "pending": pending,
            "combined_percent": 100 * sum(r["score"] for r in scored) / len(rows) if rows and not pending else None}


def allocate(total: int, weights: list[float]) -> list[int]:
    if not weights:
        return []
    amount = [total * w / sum(weights) for w in weights]
    result = [math.floor(x) for x in amount]
    for index in sorted(range(len(amount)), key=lambda i: amount[i] - result[i], reverse=True)[:total - sum(result)]:
        result[index] += 1
    return result


STAGES = [("Diagnóstico inicial", .08, "Responde preguntas sin consultar las fuentes para detectar vacíos."),
          ("Conceptos fundamentales", .24, "Empieza por requisitos previos confirmados y temas marcados como fundamentales."),
          ("Estudio de temas prioritarios", .20, "Explica cada idea con tus palabras y comprueba el original."),
          ("Práctica activa", .20, "Alterna comprensión y aplicación; vuelve después a las dificultades."),
          ("Evaluación por temas", .08, "Comprueba las unidades con preguntas de diferentes tipos."),
          ("Simulacro final", .13, "Responde un examen sin consultar la guía y con tiempo límite."),
          ("Repaso de errores", .07, "Repite errores y repasa el resumen final.")]


def build_plan(db: Database, minutes: int, previous=None) -> dict:
    if not 15 <= minutes <= 1440:
        raise ValueError("Elige de 15 minutos a 24 horas.")
    stats = sorted(topic_stats(db).values(), key=lambda t: -t["priority"])
    stage_minutes = allocate(minutes, [s[1] for s in STAGES])
    per_topic = allocate(stage_minutes[1] + stage_minutes[2], [s["priority"] for s in stats])
    now = time.time()
    return {"started": previous["started"] if previous else now,
            "deadline": previous["deadline"] if previous else now + minutes * 60,
            "minutes": minutes, "updated": now,
            "stages": [{"name": s[0], "minutes": m, "description": s[2]} for s, m in zip(STAGES, stage_minutes)],
            "topics": [{"id": s["id"], "title": s["title"], "minutes": m, "priority": round(s["priority"], 2)} for s, m in zip(stats, per_topic)],
            "completed": previous.get("completed", []) if previous else []}


def revise_plan(db: Database) -> dict:
    previous = db.get("plan")
    if not previous:
        raise ValueError("Crea primero un plan.")
    remaining = max(0, math.ceil((previous["deadline"] - time.time()) / 60))
    plan = build_plan(db, max(15, remaining), previous)
    pending = [i for i in range(len(STAGES)) if i not in previous["completed"]]
    portions = allocate(remaining, [STAGES[i][1] for i in pending])
    by_index = dict(zip(pending, portions))
    for i, stage in enumerate(plan["stages"]):
        stage["minutes"] = by_index.get(i, 0)
    stats = topic_stats(db)
    total = plan["stages"][1]["minutes"] + plan["stages"][2]["minutes"]
    amounts = allocate(total, [stats[t["id"]]["priority"] for t in plan["topics"]])
    for topic, minutes in zip(plan["topics"], amounts):
        topic["minutes"] = minutes
    db.set("plan", plan)
    return plan


def results_csv(db: Database) -> str:
    rows = db.all("""SELECT a.id,t.title tema,q.prompt pregunta,q.kind tipo,a.response respuesta,
        a.score puntuacion,a.graded_by correccion,a.feedback comentario,a.exam_id simulacro,a.created fecha_utc
        FROM attempts a JOIN questions q ON q.id=a.question_id JOIN topics t ON t.id=q.topic_id ORDER BY a.id""")
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=list(rows[0]) if rows else ["id", "tema", "pregunta", "puntuacion"])
    writer.writeheader()
    for row in rows:
        # Spreadsheet exports must not interpret document text as formulas.
        writer.writerow({k: ("'" + v if isinstance(v, str) and v.startswith(("=", "+", "-", "@")) else v) for k, v in row.items()})
    return "\ufeff" + output.getvalue()
