"""Local, dependency-free server for explanations and questions."""
from __future__ import annotations

import argparse
import threading
import urllib.parse
import urllib.request
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from course_content import LESSONS

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"
DOCUMENTS = {s["document"] for lesson in LESSONS for s in lesson["sources"]}
STATIC = {"/": "index.html", "/index.html": "index.html", "/styles.css": "styles.css",
          "/app.js": "app.js", "/course.js": "course.js"}
HEALTH = b"study-page-v2"


class StudyHandler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, ".js": "application/javascript; charset=utf-8", ".css": "text/css; charset=utf-8"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC), **kwargs)

    def translate_path(self, path):
        try:
            route = urllib.parse.unquote(urllib.parse.urlsplit(path).path, errors="strict")
        except (ValueError, UnicodeDecodeError):
            return str(PUBLIC / "__not_found__")
        if route in STATIC:
            return str(PUBLIC / STATIC[route])
        if route.startswith("/material/"):
            name = route.removeprefix("/material/")
            if name in DOCUMENTS and Path(name).name == name:
                target = (ROOT / name).resolve()
                if target.parent == ROOT and target.is_file():
                    return str(target)
        return str(PUBLIC / "__not_found__")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'")
        super().end_headers()

    def do_GET(self):
        if self.path == "/_study_health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(HEALTH)))
            self.end_headers()
            self.wfile.write(HEALTH)
            return
        super().do_GET()

    def list_directory(self, path):
        self.send_error(404, "Not found")
        return None

    def log_message(self, format, *args):
        pass


def server_ready(port=8501):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(f"http://127.0.0.1:{port}/_study_health", timeout=1) as response:
            return response.status == 200 and response.read() == HEALTH
    except OSError:
        return False


def main():
    parser = argparse.ArgumentParser(description="Explicaciones y preguntas de redes neuronales, en localhost.")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--port", type=int, default=8501)
    args = parser.parse_args()
    url = f"http://127.0.0.1:{args.port}"
    if server_ready(args.port):
        print(f"La página ya está abierta: {url}", flush=True)
        if not args.no_browser:
            webbrowser.open(url)
        return
    if not (PUBLIC / "course.js").is_file():
        from build_course import build
        build()
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), StudyHandler)
    except OSError as exc:
        raise SystemExit(f"No se pudo abrir {url}: {exc}. Cierra la versión anterior y vuelve a iniciar.") from exc
    print(f"Explicaciones y preguntas listas en {url}", flush=True)
    print("Para cerrar, presiona Ctrl+C en esta ventana.", flush=True)
    if not args.no_browser:
        threading.Timer(.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
