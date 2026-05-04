from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

DOCS   = r'c:\Users\kampomah\Desktop\my_personalphd_website\docs'
PREFIX = '/my_personalphd_website'
PORT   = 8080

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == PREFIX or self.path.startswith(PREFIX + '/'):
            self.path = self.path[len(PREFIX):] or '/'
        super().do_GET()

    def do_HEAD(self):
        if self.path == PREFIX or self.path.startswith(PREFIX + '/'):
            self.path = self.path[len(PREFIX):] or '/'
        super().do_HEAD()

    def log_message(self, *a):
        pass  # suppress console noise

os.chdir(DOCS)
print(f'\n  Open this in your browser:\n  http://localhost:{PORT}/my_personalphd_website/\n')
HTTPServer(('', PORT), Handler).serve_forever()
