# MeanderAPI

A Python wrapper for interacting with the Meander platform API. Easily manage authentication, search for quests, filter by genres, download quest files, and manage user interactions like voting, liking, or disliking content.

---

## Features

* **Flexible Authentication:** Supports token-based auth, Google Auth, and Guest mode.
* **Quest Management:** Fetch all quests, search by keywords/genres, or retrieve specific quests by ID.
* **Downloads:** Download quest files directly to your local system.
* **Social Engagement:** Cast votes, like, dislike, or unvote quests (requires authenticated session).

---

## Usage Example

Here is a comprehensive example demonstrating how to initialize the client, authenticate, browse quests, download them, and interact with the voting system.

```python
from MeanderAPI import client, quests, genres

# --- Authentication Methods ---

# 1. Auth by token (you can get it by using google auth)
user = client.new_auth_by_token("MeanderToken")

# 2. Guest mode (limited access)
user = client.new_guest()

# 3. Meander google auth
user = client.new_google_auth()


# --- Quest Discovery ---

# Get all available quests
print(quests.get_quests(user))

# Get a specific quest by its unique ID
print(quests.get_quest_by_id(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"))

# Download a quest file directly to your local path
quests.download_quest(
    user, 
    quests.get_quest_by_id(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"), 
    r"C:\Users\Deniz\Desktop\MeanderAPI\mnd.mnd"
)

# Search for quests with specific criteria (Query, Genre, Author/ID)
print(quests.get_quests_by_search(user, "test", genres.Adventure, "27ed560e-6a0f-4e67-bb7b-ce291e89f075"))


# --- Social & Voting Interactions ---
# Note: The following methods require an authenticated user (not Guest).

# Check your current vote on a quest
print(quests.get_my_vote(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Remove your vote from a quest
print(quests.unvote(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Like a quest
print(quests.like(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Dislike a quest
print(quests.dislike(user, quests.get_quest_by_id(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))
