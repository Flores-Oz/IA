from __future__ import annotations

import hashlib
import os
import re
import shutil
import statistics
import unicodedata
from pathlib import Path

import pymupdf as fitz

from .database import Database


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^\w]+", " ", text).strip()


def ocr_directory() -> str | None:
    candidates = [os.environ.get("TESSDATA_PREFIX", "")]
    executable = shutil.which("tesseract")
    if executable:
        candidates.append(str(Path(executable).parent / "tessdata"))
        candidates.append(str(Path(executable).parent.parent / "share" / "tessdata"))
    candidates += [r"C:\Program Files\Tesseract-OCR\tessdata", "/usr/share/tesseract-ocr/5/tessdata", "/usr/share/tessdata"]
    for candidate in candidates:
        if candidate and Path(candidate).is_dir() and list(Path(candidate).glob("*.traineddata")):
            return candidate
    return None


def guess_heading(page, text: str, fallback: str) -> str:
    candidates = []
    try:
        blocks = page.get_text("dict")["blocks"]
        lines = []
        for block in blocks:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                value = " ".join(s["text"].strip() for s in spans).strip()
                if value:
                    lines.append((value, max(s["size"] for s in spans), line["bbox"][1]))
        sizes = [size for _, size, _ in lines]
        median = statistics.median(sizes) if sizes else 0
        for value, size, y in lines:
            if 4 <= len(value) <= 140 and not re.fullmatch(r"[\W\d_]+", value):
                if y < page.rect.height * .38 or size > median * 1.15:
                    candidates.append((size + (8 if y < page.rect.height * .25 else 0), -y, value))
    except (RuntimeError, ValueError, KeyError):
        pass
    if candidates:
        heading = max(candidates)[2]
    else:
        heading = next((line.strip() for line in text.splitlines() if 4 <= len(line.strip()) <= 140), fallback)
    heading = re.sub(r"^[\s•·\-–\d.()]+", "", heading).strip()
    if normalize(heading) in {"contenido", "indice", "pagina", "universidad", "ejemplo", "ejemplos", "continuacion"}:
        heading = fallback
    return heading or fallback


def import_pdf(db: Database, data: bytes, name: str, use_ocr=False, language="spa+eng") -> dict:
    sha = hashlib.sha256(data).hexdigest()
    existing = db.one("SELECT * FROM documents WHERE sha=?", (sha,))
    if existing:
        return {**existing, "duplicate": True}
    # Check the actual file; an extension alone never establishes PDF validity.
    try:
        pdf = fitz.open(stream=data, filetype="pdf")
    except Exception as exc:
        raise ValueError(f"No se pudo abrir {name}: {exc}") from exc
    pages, warnings = [], []
    with pdf:
        if pdf.needs_pass:
            raise ValueError("El PDF tiene contraseña. Guarda una copia desbloqueada e impórtala.")
        if not pdf.page_count:
            raise ValueError("El PDF no contiene páginas.")
        page_count = pdf.page_count
        tessdata = ocr_directory() if use_ocr else None
        if use_ocr and not tessdata:
            warnings.append("OCR no disponible: instala Tesseract y los idiomas solicitados, o configura TESSDATA_PREFIX.")
        for index in range(page_count):
            method, warning, text, heading = "texto", "", "", Path(name).stem
            try:
                page = pdf[index]
                text = page.get_text("text", sort=True).strip()
                if len(re.sub(r"\W", "", text)) < 30:
                    if use_ocr and tessdata:
                        try:
                            tp = page.get_textpage_ocr(language=language, dpi=200, full=True, tessdata=tessdata)
                            text = page.get_text("text", textpage=tp, sort=True).strip()
                            method = "OCR local"
                        except Exception as exc:
                            warning = f"OCR falló: {exc}"
                    if len(re.sub(r"\W", "", text)) < 30:
                        warning = warning or "Texto insuficiente: página escaneada, ilustración o contenido muy breve. Revisa la imagen original."
                if "\ufffd" in text and text.count("\ufffd") > max(3, len(text) * .03):
                    warning = "La codificación del texto parece dañada. Comprueba el original; prueba una copia escaneada con OCR."
                heading = guess_heading(page, text, Path(name).stem)
            except Exception as exc:
                warning = f"Error de extracción: {exc}"
                method = "error"
            if warning:
                warnings.append(f"Página {index + 1}: {warning}")
            pages.append((index + 1, text, heading, method, warning))
    extracted = sum(1 for _, text, _, method, warning in pages if text and not warning and method != "error")
    status = "completo" if extracted == page_count else ("parcial" if any(p[1] for p in pages) else "sin texto")
    stored = db.data_dir / "documents" / f"{sha}.pdf"
    import json
    wrote_file = False
    try:
        with db.connect() as conn:
            conn.execute("BEGIN IMMEDIATE")
            concurrent = conn.execute("SELECT * FROM documents WHERE sha=?", (sha,)).fetchone()
            if concurrent:
                return {**dict(concurrent), "duplicate": True}
            stored.write_bytes(data)
            wrote_file = True
            doc_id = conn.execute("INSERT INTO documents(sha,name,stored_path,page_count,extracted_pages,status,warnings) VALUES (?,?,?,?,?,?,?)",
                                  (sha, Path(name).name, str(stored), page_count, extracted, status, json.dumps(warnings, ensure_ascii=False))).lastrowid
            for number, text, heading, method, warning in pages:
                page_id = conn.execute("INSERT INTO pages(document_id,number,text,heading,method,warning) VALUES (?,?,?,?,?,?)",
                                       (doc_id, number, text, heading, method, warning)).lastrowid
                if text.strip() and method != "error":
                    normalized = normalize(heading)
                    conn.execute("INSERT OR IGNORE INTO topics(title,normalized) VALUES (?,?)", (heading, normalized))
                    topic_id = conn.execute("SELECT id FROM topics WHERE normalized=?", (normalized,)).fetchone()[0]
                    conn.execute("INSERT OR IGNORE INTO topic_pages VALUES (?,?)", (topic_id, page_id))
    except Exception:
        if wrote_file:
            stored.unlink(missing_ok=True)
        raise
    return {**db.one("SELECT * FROM documents WHERE id=?", (doc_id,)), "duplicate": False}


def repetitions(db: Database) -> list[dict]:
    """Exact normalized paragraphs, never a claim of semantic equivalence."""
    groups: dict[str, dict] = {}
    for page in db.all("SELECT p.*,d.name FROM pages p JOIN documents d ON d.id=p.document_id"):
        # Text extraction in slides often creates one line per sentence.
        for part in re.split(r"\n\s*\n|(?<=[.!?])\s+", page["text"]):
            key = normalize(part)
            if len(key) < 65:
                continue
            group = groups.setdefault(key, {"text": part.strip(), "sources": []})
            ref = {"page_id": page["id"], "document_id": page["document_id"], "document": page["name"], "page": page["number"]}
            if ref not in group["sources"]:
                group["sources"].append(ref)
    return sorted([g for g in groups.values() if len({s["document_id"] for s in g["sources"]}) > 1],
                  key=lambda g: -len(g["sources"]))


def retry_ocr(db: Database, document_id: int, language="spa+eng") -> dict:
    """Retry warned pages, preserving old text and IDs used by saved references."""
    import json
    tessdata = ocr_directory()
    if not tessdata:
        raise ValueError("No se encontraron los datos locales de Tesseract. Configura TESSDATA_PREFIX.")
    document = db.one("SELECT * FROM documents WHERE id=?", (document_id,))
    if not document:
        raise ValueError("Documento no encontrado.")
    candidates = db.all("SELECT * FROM pages WHERE document_id=? AND warning!=''", (document_id,))
    with fitz.open(document["stored_path"]) as pdf:
        for old in candidates:
            warning = ""
            try:
                page = pdf[old["number"] - 1]
                tp = page.get_textpage_ocr(language=language, dpi=200, full=True, tessdata=tessdata)
                text = page.get_text("text", textpage=tp, sort=True).strip()
                if len(re.sub(r"\W", "", text)) < 30:
                    warning = "OCR local: texto insuficiente; revisa la página original."
                combined = old["text"]
                if text not in combined:
                    combined = (combined + "\n\n" + text).strip()
                db.execute("UPDATE pages SET text=?,method='texto + OCR local',warning=? WHERE id=?", (combined, warning, old["id"]))
                if combined and not db.one("SELECT 1 FROM topic_pages WHERE page_id=?", (old["id"],)):
                    heading = guess_heading(page, combined, Path(document["name"]).stem)
                    db.execute("INSERT OR IGNORE INTO topics(title,normalized) VALUES (?,?)", (heading, normalize(heading)))
                    topic = db.one("SELECT id FROM topics WHERE normalized=?", (normalize(heading),))
                    db.execute("INSERT OR IGNORE INTO topic_pages VALUES (?,?)", (topic["id"], old["id"]))
            except Exception as exc:
                db.execute("UPDATE pages SET warning=? WHERE id=?", (f"OCR falló: {exc}", old["id"]))
    pages = db.all("SELECT * FROM pages WHERE document_id=?", (document_id,))
    warnings = [f"Página {p['number']}: {p['warning']}" for p in pages if p["warning"]]
    extracted = sum(bool(p["text"]) and not p["warning"] for p in pages)
    status = "completo" if extracted == len(pages) else ("parcial" if any(p["text"] for p in pages) else "sin texto")
    db.execute("UPDATE documents SET status=?,extracted_pages=?,warnings=? WHERE id=?", (status, extracted, json.dumps(warnings, ensure_ascii=False), document_id))
    return db.one("SELECT * FROM documents WHERE id=?", (document_id,))


def suggested_dependencies(db: Database) -> list[dict]:
    """A mention suggests a relationship; the user must confirm prerequisites."""
    topics = db.topics()
    suggestions = []
    for dependent in topics:
        body = normalize(" ".join(p["text"] for p in db.sources(dependent["id"])))
        for base in topics:
            term = base["normalized"]
            if base["id"] != dependent["id"] and 8 <= len(term) <= 80 and f" {term} " in f" {body} ":
                suggestions.append({"prerequisite_id": base["id"], "dependent_id": dependent["id"],
                                    "reason": "El título del primer tema aparece en el contenido del segundo. Relación propuesta; verifica si es un requisito previo."})
    return suggestions[:100]
