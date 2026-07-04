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
