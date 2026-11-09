import json
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request
from http.server import ThreadingHTTPServer

from course_content import LESSONS
from run_local import HEALTH, ROOT, StudyHandler


class ContentTests(unittest.TestCase):
    def test_each_topic_has_substantial_explanation_and_four_questions(self):
        self.assertEqual(len(LESSONS), 13)
        for lesson in LESSONS:
            with self.subTest(topic=lesson["id"]):
                self.assertTrue(lesson["intro"])
                self.assertGreaterEqual(len(lesson["sections"]), 3)
                self.assertEqual(len(lesson["questions"]), 4)
                self.assertTrue(lesson["sources"])
                self.assertGreater(sum(len(" ".join(s["paragraphs"])) for s in lesson["sections"]), 700)

    def test_correct_options_and_open_answer_criteria_are_valid(self):
        for lesson in LESSONS:
            for q in lesson["questions"]:
                self.assertTrue(q["explanation"])
                if q["kind"] == "choice":
                    self.assertEqual(len(q["options"]), 4)
                    self.assertEqual(len(set(q["options"])), 4)
                    self.assertIn(q["answer"], range(4))
                else:
                    self.assertTrue(q["answer"])
                    self.assertGreaterEqual(len(q["criteria"]), 3)

    def test_built_content_matches_source(self):
        data = (ROOT / "public" / "course.js").read_text(encoding="utf-8")
        payload = json.loads(data.removeprefix("window.COURSE = ").rstrip("\n;"))
        self.assertEqual(len(payload["lessons"]), 13)
        ids = [q["id"] for l in payload["lessons"] for q in l["questions"]]
        self.assertEqual(len(ids), 52)
        self.assertEqual(len(set(ids)), 52)
        for original, built in zip(LESSONS, payload["lessons"]):
            self.assertEqual(original["sections"], built["sections"])
            self.assertEqual(original["sources"], built["sources"])

    def test_references_match_existing_files_and_page_counts(self):
        counts = {"15.1.0 Normalización.pptx.pdf": 11,
                  "16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf": 15,
                  "17.1 Función de activación.pptx.pdf": 14, "18.1 Clasificación.pptx.pdf": 9,
                  "19.1 Clasificación de imagenes.pptx.pdf": 7,
                  "20.2 Redes neuronales convolucionales.pptx.pdf": 19,
                  "RedesNeuronalesBasicas.pdf": 3,
                  "20.4 Ejercicio de repaso redes neuronales.docx.pdf": 2,
                  "Preguntas basicas redes neuronales convolucionales.pdf": 1,
                  "Informe_Neuronas_Clasificacion_Imagenes.pdf": 2,
                  "19.3 Laboratorio analisis de una CNN.doc.pdf": 1}
        for lesson in LESSONS:
            for source in lesson["sources"]:
                self.assertTrue((ROOT / source["document"]).is_file())
                self.assertTrue(all(1 <= p <= counts[source["document"]] for p in source["pages"]))

    def test_page_has_no_model_configuration_or_external_assets(self):
        html = (ROOT / "public" / "index.html").read_text(encoding="utf-8")
        js = (ROOT / "public" / "app.js").read_text(encoding="utf-8")
        self.assertNotIn("Ollama", html + js)
        self.assertNotIn("Simulacro", html + js)
        self.assertNotIn("https://", html + js)
        self.assertNotIn("fetch(", js)
        self.assertNotIn("XMLHttpRequest", js)


class LocalServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), StudyHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"
        cls.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get(self, path):
        return self.opener.open(self.base + path, timeout=3)

    def test_page_and_assets_are_served(self):
        for route in ("/", "/index.html", "/styles.css", "/app.js", "/course.js"):
            with self.subTest(route=route), self.get(route) as response:
                self.assertEqual(response.status, 200)
                self.assertGreater(len(response.read()), 100)
        with self.get("/_study_health") as response:
            self.assertEqual(response.read(), HEALTH)

    def test_headers_block_external_resources_and_server_binds_loopback(self):
        with self.get("/") as response:
            self.assertIn("default-src 'self'", response.headers["Content-Security-Policy"])
            self.assertEqual(response.headers["Cache-Control"], "no-store")
            self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(self.server.server_address[0], "127.0.0.1")

    def test_pdf_link_returns_actual_document(self):
        name = LESSONS[0]["sources"][0]["document"]
        with self.get("/material/" + urllib.parse.quote(name)) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get_content_type(), "application/pdf")
            self.assertTrue(response.read(5).startswith(b"%PDF"))

    def test_storage_and_traversal_are_not_served(self):
        for path in ("/app_data/study.sqlite3", "/.venv/", "/../README.md", "/material/../README.md", "/material/%2e%2e%2fREADME.md", "/material/not-listed.pdf", "/%00"):
            with self.subTest(path=path):
                with self.assertRaises(urllib.error.HTTPError) as result:
                    self.get(path)
                self.assertEqual(result.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
