import typing

class User:
    """Represents a user within the MeanderAPI system.
    Provides access to user-specific data, actions, and account attributes.

    Attributes:
        id (str): Unique identifier of the user (UUID).
        fullName (str): The user's display name.
        avatarUrl (str): URL to the user's avatar image.
        createdAt (str): ISO timestamp of account creation.
        bio (str): User's profile biography.
        isVerified (bool): Verification status of the user.
        role (str): System role (e.g., 'user', 'admin').
        streakCount (int): Current activity streak count.
        totalPlaytimeSeconds (str/int): Total time spent playing in seconds.
        followersCount (int): Total number of followers.
        followingCount (int): Total number of followed users.
    """
    def __init__(self, data: dict) -> None:
        self.id: str = data.get('id', '')
        self.fullName: str = data.get('full_name', 'UNKNOWN USER')
        self.avatarUrl: str = data.get('avatar_url', 'https://lh3.googleusercontent.com/a/ACg8ocJfDUKLf72apOo96-_TOUQGjxBnPJxR7nkfCiMwApa-_ujf3ycB=s96-c')
        self.createdAt: str = data.get('created_at', '1970-1-1T00:00:00.000Z')
        self.bio: str = data.get('bio', '')
        self.isVerified: bool = data.get('is_verified', False)
        self.role: str = data.get('role', 'user')
        self.streakCount: int = data.get('streak_count', 0)
        self.totalPlaytimeSeconds: int = data.get('total_quests_playtime_seconds', 0)
        self.followersCount: int = data.get('followers_count', 0)
        self.followingCount: int = data.get('following_count', 0)
    
    def __repr__(self):
        avatarUrl = self.avatarUrl[:50] + "..."
        return f"""MeanderAPI.types.User(
    id={self.id!r},
    fullName={self.fullName!r},
    bio={self.bio!r},
    role={self.role!r},
    followersCount={self.followersCount!r},
    followingCount={self.followingCount!r},
    avatarUrl={avatarUrl!r},
    createdAt={self.createdAt!r},
    isVerified={self.isVerified!r},
    streakCount={self.streakCount!r},
    totalPlaytimeSeconds={self.totalPlaytimeSeconds!r}
)"""
