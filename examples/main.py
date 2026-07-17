from MeanderAPI import Client, Genres, Quests

# Auth by token you can get it by using google auth
user = Client.TokenAuth("MeanderToken")

# Guest mode
user = Client.Guest()

# Meander google auth
user = Client.GoogleAuth()

# Get all quests
print(Quests.getQuests(user))

# Get quest by id
print(Quests.getQuestById(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"))

# Download quest
Quests.downloadQuest(user, quests.getQuestById(user, "ba0b5e8d-0d4f-4368-af9f-2564bc00c07d"), r"C:\Users\Deniz\Desktop\MeanderAPI\mnd.mnd")

# Get quest by search
print(Quests.getQuestsBySearch(user, "test", Genres.Adventure, "27ed560e-6a0f-4e67-bb7b-ce291e89f075"))

# Get my vote quest (Auth required)
print(Quests.getMyVote(user, Quests.getQuestById(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Unvote quest (Auth required)
print(Quests.unvote(user, Quests.getQuestById(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Like quest (Auth required)
print(quests.like(user, Quests.getQuestById(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Dislike quest (Auth required)
print(Quests.dislike(user, Quests.getQuestById(user, "7915972f-92bb-4464-b14d-c1a279cd8a26")))

# Get user profile
print(Client.getProfile(user, "27ed560e-6a0f-4e67-bb7b-ce291e89f075"))

# Get user profile achievements
print(Client.getProfileAdvancements(user, Client.getProfile(user, "27ed560e-6a0f-4e67-bb7b-ce291e89f075")))

# Toggle follow (Auth required)
print(Client.toggleFollow(user, Client.getProfile(user, "f7e7709b-ce64-4aea-ab65-4d1c11c31756")))

# Update streak (auth required)
print(Client.updateStreak(user))

# Update profile (Auth required)
print(Client.updateProfile(user, "test name", "test bio", "path_to_avatar_jpeg"))

# Get featured quests (Auth required)
print(Quests.getFeaturedQuests(user))

# Get recent quests (Auth required)
print(Quests.getRecentQuests(user))

# Get like genres quests (Auth required)
print(Quests.getLikeGenresQuests(user))
