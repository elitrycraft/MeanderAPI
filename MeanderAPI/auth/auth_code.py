from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class GoogleAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        code_list = query_params.get("code")
        
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        if code_list:
            self.server.received_code = code_list[0]
            response = "<h1>Successfully</h1><p>Auth code found. You can close browser.</p>"
            self.wfile.write(response.encode("utf-8"))
            self.server.should_stop = True
        else:
            response = "<h1>Error</h1><p>No auth code</p>"
            self.wfile.write(response.encode("utf-8"))

    def log_message(self, format, *args):
        return

def get_code():
    server_address = ("127.0.0.1", 61222)
    httpd = HTTPServer(server_address, GoogleAuthHandler)
    httpd.should_stop = False
    httpd.received_code = None
    while not httpd.should_stop:
        httpd.handle_request()
    httpd.server_close()
    return httpd.received_code
