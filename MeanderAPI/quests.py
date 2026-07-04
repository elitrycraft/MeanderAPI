import requests, json

class quests:
    def get_quests(client):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }

        resp = requests.get("https://backend.meander.sbs/quests", headers=headers)
        return resp.json()
    def get_quest_by_id(client, quest_id):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }

        resp = requests.get("https://backend.meander.sbs/quests/" + quest_id, headers=headers)
        return resp.json()
    def download_quest(client, quest, path):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }

        quest_url = quest["download_url"]
        
        resp = requests.get(quest_url, headers=headers)
        with open(path, "wb") as f:
            f.write(resp.content)
    def get_quests_by_search(client, query=None, genre=None, author_id=None):
        params = {}
        if query:
            params["search"] = query
        if genre:
            params["genre"] = genre
        if author_id:
            params["author_id"] = author_id
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        resp = requests.get("https://backend.meander.sbs/quests", params=params, headers=headers)
        return resp.json()

    def like(client, quest):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        quest_id = quest["id"]
        resp = requests.post(
            f"https://backend.meander.sbs/quests/{quest_id}/vote",
            headers=headers,
            json={"action": "set", "is_like": True}
        )
        return resp.json()
    def dislike(client, quest):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        quest_id = quest["id"]
        resp = requests.post(
            f"https://backend.meander.sbs/quests/{quest_id}/vote",
            headers=headers,
            json={"action": "set", "is_like": False}
        )
        return resp.json()
    def unvote(client, quest):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        quest_id = quest["id"]
        resp = requests.post(
            f"https://backend.meander.sbs/quests/{quest_id}/vote",
            headers=headers,
            json={"action": "remove"}
        )
        return resp.json()
    def get_my_vote(client, quest):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        quest_id = quest["id"]
        resp = requests.get(
            f"https://backend.meander.sbs/quests/{quest_id}/my-vote",
            headers=headers
        )
        return resp.json()
