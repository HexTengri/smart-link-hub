from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Burası bizim "Yönlendirme" mantığımız olacak
        # Şimdilik sistemin çalıştığını test ediyoruz
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('<h1>System Active: Smart-Link-Hub</h1>'.encode())
        return
