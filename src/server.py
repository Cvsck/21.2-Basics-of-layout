import os
import http.server
import socketserver

PORT = 8000
HTML_FILE = os.path.join(os.path.dirname(__file__), "contacts.html")


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Главная страница
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(HTML_FILE, "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))

        # Игнорируем `favicon.ico`
        elif self.path == "/favicon.ico":
            self.send_response(404)
            self.end_headers()
            return

        # Отправка статических файлов (CSS, иконки)
        elif self.path.startswith("/css/") or self.path.startswith("/icons/"):
            self.send_static_file(self.path[1:])  # Убираем `/` в начале

        # Ошибка 404 для остальных запросов
        else:
            self.send_error(404, "Страница не найдена")

    def send_static_file(self, file_path):
        """Отправляет статические файлы (CSS, изображения, JS)"""
        try:
            with open(file_path, "rb") as file:
                self.send_response(200)
                if file_path.endswith(".css"):
                    self.send_header("Content-Type", "text/css")
                elif file_path.endswith(".svg"):
                    self.send_header("Content-Type", "image/svg+xml")
                elif file_path.endswith(".ico"):
                    self.send_header("Content-Type", "image/x-icon")
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "Файл не найден")


# Запуск сервера
httpd = socketserver.TCPServer(("", PORT), MyHandler)
print(f"✅ Сервер запущен на порту {PORT}")
httpd.serve_forever()
