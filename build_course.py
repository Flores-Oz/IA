"""Build the local page content. Uses only the Python standard library."""
import json
from pathlib import Path
from course_content import LESSONS


def build():
    for lesson in LESSONS:
        for i, question in enumerate(lesson["questions"], 1):
            question["id"] = f"{lesson['id']}-{i}"
    payload = {"title": "Redes neuronales", "lessons": LESSONS}
    destination = Path(__file__).resolve().parent / "public" / "course.js"
    destination.write_text("window.COURSE = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(f"Preparados {len(LESSONS)} temas y {sum(len(l['questions']) for l in LESSONS)} preguntas.")


if __name__ == "__main__":
    build()
