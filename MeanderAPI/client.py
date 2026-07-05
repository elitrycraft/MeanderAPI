import requests, json
import webbrowser

google_auth_url = (
    "https://accounts.google.com/o/oauth2/v2/auth?"
    "client_id=410112450155-mgd0ic4883lg6ic2e2ljrnipt6n2jrdc.apps.googleusercontent.com&"
    "redirect_uri=http://localhost:61222&"
    "response_type=code&"
    "scope=openid%20email%20profile"
)

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

import requests

def code_to_token(code, client_secret=None):
    data = {
        "code": code,
        "client_id": "410112450155-mgd0ic4883lg6ic2e2ljrnipt6n2jrdc.apps.googleusercontent.com",
        "redirect_uri": "http://localhost:61222",
        "client_secret": "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",
        "grant_type": "authorization_code",
    }

    if client_secret:
        data["client_secret"] = client_secret

    resp = requests.post("https://oauth2.googleapis.com/token", data=data)

    if resp.status_code == 200:
        return resp.json().get("id_token")
    else:
        print(resp.text)
        return "NoToken"

import requests, json

def get_token(id_token):
    resp = requests.post(
        "https://backend.meander.sbs/auth/google/token",
        json={"idToken": id_token}
    )

    if resp.status_code == 200:
        meander_token = resp.json()["token"]
        return meander_token
    else:
        print(f"Error: {resp.text}")
        return "NoToken"


class client:
    def new_guest():
        return "NoToken"
    def new_auth_by_token(token):
        return token
    def new_google_auth():
        webbrowser.open(google_auth_url)
        code = get_code()
        token = code_to_token(code)
        token_meander = get_token(token)
        return token_meander
    def get_profile(client, profile_id):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }

        resp = requests.get(f"https://backend.meander.sbs/profiles/{profile_id}", headers=headers)
        return resp.json()
