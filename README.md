# MeanderAPI

A python library for interact with Meander API
---

## Features

* Supports Google auth
* Get all quest list without auth
* Download quests without auth
* Auth by token

---

# Install

```bash
pip install MeanderAPI
```

# For more docs: (THIS)[https://github.com/elitrycraft/MeanderAPI/wiki]

## Usage Example

Here is a comprehensive example demonstrating how to initialize the client, authenticate, browse quests, download them, and interact with the voting system.

```python
from MeanderAPI import client, quests, genres

# Auth by token you can get it by using google auth
user = client.new_auth_by_token("MeanderToken")

# Guest mode
user = client.new_guest()

# Meander google auth
user = client.new_google_auth()

# Get all quests
print(quests.get_quests(user))

# Get quest by id
print(quests.get_quest_by_id(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"))

# Download quest
quests.download_quest(user, quests.get_quest_by_id(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"), r"C:\Users\Deniz\Desktop\MeanderAPI\mnd.mnd")

# Get quest by search
print(quests.get_quests_by_search(user, "test", genres.Adventure, "27ed560e-6a0f-4e67-bb7b-ce291e89f075"))

# Get my vote quest (Auth required)
print(quests.get_my_vote(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Unvote quest (Auth required)
print(quests.unvote(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Like quest (Auth required)
print(quests.like(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Dislike quest (Auth required)
print(quests.dislike(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))
```
