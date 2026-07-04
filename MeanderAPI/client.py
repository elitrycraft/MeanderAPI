import requests, json
import webbrowser
from .auth import auth_code
from .auth import google_token
from .auth import meander_token

google_auth_url = (
    "https://accounts.google.com/o/oauth2/v2/auth?"
    "client_id=410112450155-mgd0ic4883lg6ic2e2ljrnipt6n2jrdc.apps.googleusercontent.com&"
    "redirect_uri=http://localhost:61222&"
    "response_type=code&"
    "scope=openid%20email%20profile"
)

class client:
    def new_guest():
        return "NoToken"
    def new_auth_by_token(token):
        return token
    def new_google_auth():
        webbrowser.open(google_auth_url)
        code = auth_code.get_code()
        token = google_token.code_to_token(code)
        token_meander = meander_token.get_token(token)
        return token_meander
