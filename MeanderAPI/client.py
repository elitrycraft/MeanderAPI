import httpx
import typing
from .types import User
from types import TracebackType

class GuestClient:
    """Represents an unauthenticated guest session within the MeanderAPI.
    Provides limited access to public endpoints that do not require user credentials.
    """
    def __init__(self, name: str, base_url: str = "https://backend.meander.sbs"):
        """Initializes a new Guest session.

        Args:
            name (str): Name of your MiniApp/UserBot.
            base_url (str, optional): The base URL for the MeanderAPI endpoints. Defaults to the official production server.
        """
        self.name = name
        self.baseUrl = base_url
    
    async def __aenter__(self) -> "GuestClient":
        return self

    async def __aexit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]], 
        exc_val: typing.Optional[BaseException], 
        exc_tb: typing.Optional[TracebackType]
    ) -> bool:
        return False
    
    async def getUserProfile(self, id: str) -> User:
        """Fetches a user profile from the API by its unique identifier.

        Args:
            id (str): The unique ID of the user to retrieve.

        Returns:
            User: An instance of the User class populated with profile data.

        Raises:
            Exception: If the user is not found, id is invalid or the API returns an error.
        """

        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(f'{self.baseUrl}/profiles/{id}')
                if r.json().get('error', None) == 'Invalid ID format':
                    raise Exception(f"MeanderAPI: API Error: {r.json().get('error')}")

                return User(r.json())
        except Exception as e:
            raise Exception(f'MeanderAPI: Unknown error: {e}')