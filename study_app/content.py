from __future__ import annotations

import hashlib
import json
import random
import re

from .database import Database
from .ingest import normalize

KINDS = {"choice": "Selección múltiple", "true_false": "Verdadero o falso", "short": "Respuesta corta",
         "essay": "Desarrollo", "cloze": "Completar conceptos", "problem": "Problema práctico",
         "interpretation": "Interpretación de ejemplos", "application": "Aplicación"}
DIFFICULTIES = ["Básica", "Intermedia", "Avanzada"]
OBJECTIVE = {"choice", "true_false"}
SECTIONS = ["Resumen", "Conceptos clave", "Definiciones", "Procedimientos", "Ejemplos", "Comparaciones",
            "Errores frecuentes", "Preguntas importantes", "Fórmulas o comandos", "Memorizar", "Comprender y practicar"]


def source_hash(sources: list[dict]) -> str:
    return hashlib.sha256(json.dumps([(s["id"], s["text"]) for s in sources], ensure_ascii=False).encode()).hexdigest()


def fragments(text: str) -> list[str]:
    text = re.sub(r"[ \t]+", " ", text)
    result = []
    for part in re.split(r"\n\s*\n|(?<=[.!?;])\s+", text):
        part = part.strip()
        if len(part) > 700:
            # Preserve actual contiguous characters for exact quotation validation.
            result.extend(part[i:i + 600].strip() for i in range(0, len(part), 600))
        elif len(part) >= 35:
            result.append(part)
    return result or ([text.strip()] if text.strip() else [])


def extractive_guide(sources: list[dict], level="Normal") -> dict:
    result = {key: [] for key in SECTIONS}
    max_items = {"Rápido": 3, "Normal": 7, "Profundo": 18}.get(level, 7)
    seen = set()
    for source in sources:
        for value in fragments(source["text"]):
            key = normalize(value)
            if key in seen:
                continue
            seen.add(key)
            item = {"text": value, "page_id": source["id"]}
            if len(result["Resumen"]) < max_items:
                result["Resumen"].append(item)
            classifiers = {
                "Definiciones": r"\b(es|son|define|consiste|denomina|se refiere)\b",
                "Procedimientos": r"\b(paso|primero|luego|después|procedimiento|algoritmo)\b|(?:^|\n)\d+[.)]",
                "Ejemplos": r"\b(ejemplo|supong|caso|ejercicio)\w*",
                "Comparaciones": r"\b(diferencia|mientras|compar|a diferencia)\w*",
                "Fórmulas o comandos": r"[=∑∂Σλσ]|\b(import|pip|SELECT|def |sudo|print\()",
                "Memorizar": r"\b(fórmula|definición|ley|regla|comando)\b",
                "Comprender y practicar": r"\b(calcular|aplicar|resolver|implementar|analizar|entrenar)\b",
            }
            for section, pattern in classifiers.items():
                if re.search(pattern, value, re.I) and len(result[section]) < max_items:
                    result[section].append(item)
        if len(result["Conceptos clave"]) < max_items:
            result["Conceptos clave"].append({"text": source["heading"], "page_id": source["id"]})
    return result


def add_question(db: Database, q: dict) -> int:
    signature = hashlib.sha256(f"{q['topic_id']}|{q['kind']}|{normalize(q['prompt'])}".encode()).hexdigest()
    db.execute("""INSERT OR IGNORE INTO questions(topic_id,kind,difficulty,prompt,options,answer,explanation,refs,rubric,generator,signature)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (q["topic_id"], q["kind"], q["difficulty"], q["prompt"],
        json.dumps(q.get("options", []), ensure_ascii=False), str(q["answer"]), q["explanation"],
        json.dumps(q["refs"], ensure_ascii=False), json.dumps(q["rubric"], ensure_ascii=False), q["generator"], signature))
    return db.one("SELECT id FROM questions WHERE signature=?", (signature,))["id"]


def basic_questions(db: Database, topic_id: int) -> int:
    """Honest literal recall plus open recall; application generation needs Ollama."""
    topic = db.one("SELECT * FROM topics WHERE id=?", (topic_id,))
    before = db.one("SELECT COUNT(*) n FROM questions WHERE topic_id=?", (topic_id,))["n"]
    seen = set()
    for source in db.sources(topic_id)[:3]:
        # Use an actual substring from stored text, without whitespace normalization.
        value = next((v.strip() for v in re.split(r"\n\s*\n|(?<=[.!?])\s+", source["text"]) if 70 <= len(v.strip()) <= 650), source["text"][:500].strip())
        if len(value) < 40 or normalize(value) in seen:
            continue
        seen.add(normalize(value))
        ref = [{"page_id": source["id"], "quote": value}]
        base = {"topic_id": topic_id, "difficulty": "Básica", "refs": ref, "generator": "extractivo local",
                "rubric": ["Identificar la idea principal del fragmento (50 %).", "Explicar su significado sin contradecirlo (30 %).", "Relacionarla con el tema (20 %)."]}
        words = list(dict.fromkeys(re.findall(r"\b[^\W\d_]{5,}\b", value, re.UNICODE)))
        if len(words) >= 4:
            word = max(words, key=len)
            options = [word] + [w for w in words if normalize(w) != normalize(word)][:3]
            rng = random.Random(hashlib.sha256(value.encode()).hexdigest())
            rng.shuffle(options)
            prompt = f"Completa con la palabra EXACTA del material sobre «{topic['title']}»:\n\n" + re.sub(rf"\b{re.escape(word)}\b", "________", value)
            add_question(db, {**base, "kind": "choice", "prompt": prompt, "options": options, "answer": str(options.index(word)),
                              "explanation": f"El fragmento original utiliza «{word}». Es un ejercicio de recuerdo literal, no una prueba de comprensión completa."})
            add_question(db, {**base, "kind": "cloze", "prompt": prompt, "answer": word,
                              "explanation": "Compara tu palabra con el original. La autoevaluación permite considerar variantes justificadas."})
        add_question(db, {**base, "kind": "short", "prompt": f"Recuerda y explica con tus palabras una idea central de «{topic['title']}» que se presenta en {source['document_name']}, página física {source['number']}. Relaciónala con el tema.",
                          "answer": value, "explanation": "Este fragmento es la referencia para la autoevaluación. No es una respuesta de desarrollo generada; consulta toda la página si necesitas contexto."})
    after = db.one("SELECT COUNT(*) n FROM questions WHERE topic_id=?", (topic_id,))["n"]
    return after - before


def reference(db: Database, page_id: int) -> dict | None:
    return db.one("SELECT p.*,d.name document_name,d.stored_path FROM pages p JOIN documents d ON d.id=p.document_id WHERE p.id=?", (page_id,))


def valid_evidence(items, sources: list[dict]) -> list[dict]:
    by_id = {s["id"]: s for s in sources}
    valid = []
    if not isinstance(items, list):
        return valid
    for item in items[:12]:
        if not isinstance(item, dict):
            continue
        try:
            page_id = int(item.get("page_id", 0))
        except (ValueError, TypeError):
            continue
        quote = item.get("quote", "")
        # Whitespace variations are acceptable; invented words and page numbers are not.
        if isinstance(quote, str) and len(quote.strip()) >= 15 and page_id in by_id:
            source = re.sub(r"\s+", " ", by_id[page_id]["text"])
            quote = re.sub(r"\s+", " ", quote).strip()
            if quote in source:
                valid.append({"page_id": page_id, "quote": quote})
    return valid


def context_sources(sources: list[dict], budget=15500) -> list[dict]:
    """Cover the topic across pages, with explicit truncation visible to the caller."""
    if not sources:
        return []
    if len(sources) > 12:
        indices = sorted({round(i * (len(sources) - 1) / 11) for i in range(12)})
        sources = [sources[i] for i in indices]
    share = max(200, budget // len(sources))
    return [{**s, "text": s["text"][:share]} for s in sources]


def export_guide(db: Database, topic_ids: list[int] | None = None, level="Normal") -> str:
    parts = ["# Guía de estudio local", "Las páginas indicadas son posiciones físicas del PDF, comenzando en 1.",
             "Los extractos son la fuente principal. Las explicaciones del modelo local son borradores que requieren comprobación."]
    for topic in db.topics():
        if topic_ids is not None and topic["id"] not in topic_ids:
            continue
        sources = db.sources(topic["id"])
        parts.append(f"\n## {topic['title']}")
        for section, items in extractive_guide(sources, level).items():
            if items:
                parts.append(f"\n### {section} · extractos del PDF")
                for item in items:
                    src = next(s for s in sources if s["id"] == item["page_id"])
                    parts.append(f"\n{item['text']}\n\nFuente: {src['document_name']}, p. {src['number']}.")
        guide = db.one("SELECT * FROM guides WHERE topic_id=? AND level=? AND simple=0", (topic["id"], level))
        if guide and guide["source_hash"] == source_hash(sources):
            content = json.loads(guide["content"])
            parts.append(f"\n### Borrador del modelo local {guide['model']} · {level}")
            for section, items in content.get("sections", {}).items():
                parts.append(f"\n#### {section}")
                for item in items:
                    parts.append("\n" + item["text"])
                    for ref in item["evidence"]:
                        src = reference(db, ref["page_id"])
                        if src:
                            parts.append(f"> {ref['quote']}\n\n{src['document_name']}, p. {src['number']}.")
            for item in content.get("complements", []):
                parts.append(f"\n**Complemento de IA no verificado:** {item}")
            for item in content.get("gaps", []):
                parts.append(f"\n**Información insuficiente o punto por revisar:** {item}")
    return "\n\n".join(parts)
