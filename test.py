from MeanderAPI import GuestClient
import asyncio

async def main():
    async with GuestClient(__name__) as client:
        user = await client.getUserProfile(id="27ed560e-6a0f-4e67-bb7b-ce291e89f075")
        print(user)

asyncio.run(main())