
# python3 -m http.server 8000

import http.server
import os
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

os.chdir("webroot")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving in http://localhost:{PORT}")
    httpd.serve_forever()


