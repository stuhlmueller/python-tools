#!/usr/bin/python
import SimpleHTTPServer
import SocketServer

def serve_string(content, port=8000):
    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.wfile.write(content)
    httpd = SocketServer.TCPServer(("", port), Handler)
    httpd.serve_forever()

def serve_file(filename, port=8000):
    serve_string(open(filename).read(), port)
