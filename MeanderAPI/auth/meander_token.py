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
