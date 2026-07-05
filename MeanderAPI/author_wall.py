import requests
import json

class author_wall:
    @staticmethod
    def upload_media(client, file_path):
        headers = {"Authorization": f"Bearer {client}"}
        
        with open(file_path, "rb") as f:
            files = {"file": f}
            resp = requests.post(
                "https://backend.meander.sbs/api/author-walls/upload-media",
                headers=headers,
                files=files
            )
        
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": resp.status_code, "message": resp.text}
    
    @staticmethod
    def get_posts(client, author_id, limit=10, offset=0, viewer_id=None):
        headers = {"Authorization": f"Bearer {client}"}
        params = {"limit": limit, "offset": offset}
        if viewer_id:
            params["viewer_id"] = viewer_id
        
        resp = requests.get(
            f"https://backend.meander.sbs/api/author-walls/{author_id}/posts",
            headers=headers,
            params=params
        )
        return resp.json()
    
    @staticmethod
    def get_post(client, post_id):
        headers = {"Authorization": f"Bearer {client}"}
        resp = requests.get(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}",
            headers=headers
        )
        return resp.json()
    
    @staticmethod
    def create_post(client, author_id, content, media_urls=None):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        data = {"content": content}
        if media_urls:
            data["media_urls"] = media_urls
        
        resp = requests.post(
            f"https://backend.meander.sbs/api/author-walls/{author_id}/posts",
            headers=headers,
            json=data
        )
        return resp.json()
    
    @staticmethod
    def update_post(client, post, content=None, media_urls=None):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        data = {}
        post_id = post["id"]
        if content is not None:
            data["content"] = content
        if media_urls is not None:
            data["media_urls"] = media_urls
        
        if not data:
            return {"error": 400, "message": "No fields to update"}
        
        resp = requests.put(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}",
            headers=headers,
            json=data
        )
        return resp.json()
    
    @staticmethod
    def delete_post(client, post):
        headers = {"Authorization": f"Bearer {client}"}
        post_id = post["id"]
        resp = requests.delete(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}",
            headers=headers
        )
        return resp.json()
    
    @staticmethod
    def view_post(client, post):
        headers = {"Authorization": f"Bearer {client}"}
        post_id = post["id"]
        resp = requests.post(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}/view",
            headers=headers
        )
        return resp.json()
    
    @staticmethod
    def get_comments(client, post, limit=10, offset=0):
        headers = {"Authorization": f"Bearer {client}"}
        params = {"limit": limit, "offset": offset}
        post_id = post["id"]
        
        resp = requests.get(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}/comments",
            headers=headers,
            params=params
        )
        return resp.json()
    
    @staticmethod
    def create_comment(client, post, content, parent_id=None):
        headers = {
            "Authorization": f"Bearer {client}",
            "Content-Type": "application/json"
        }
        post_id = post["id"]
        data = {"content": content}
        if parent_id:
            data["parentId"] = parent_id
        
        resp = requests.post(
            f"https://backend.meander.sbs/api/author-walls/posts/{post_id}/comments",
            headers=headers,
            json=data
        )
        return resp.json()
