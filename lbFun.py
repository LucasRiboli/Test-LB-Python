import http.server
import socketserver
import random

class LBHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        
        instances = [
            "http://localhost:5001",
            "http://localhost:5002"
        ]
        
        chosen_instance = random.choice(instances)
        self.send_response(302)
        self.send_header("Location", chosen_instance + self.path)
        self.end_headers()


with socketserver.TCPServer(("", 8080), LBHandler) as httpd:
    httpd.serve_forever()
