<div align="center">
    <h1>MeanderAPI</h1>
    <h3>A lightweight and user-friendly Python wrapper for the <a href="https://meander.sbs/">Meander</a> API.</h3>
    <a href="https://github.com/elitrycraft/MeanderAPI/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/elitrycraft/MeanderAPI?style=for-the-badge&logo=github&color=f4dbd6&logoColor=D9E0EE&labelColor=302D41"></a>
    <a href="https://github.com/elitrycraft/MeanderAPI/releases/latest">
    <img alt="Releases" src="https://img.shields.io/github/release/elitrycraft/MeanderAPI.svg?style=for-the-badge&logo=semantic-release&color=f5bde6&logoColor=D9E0EE&labelColor=302D41"/></a>
    <a href="https://pypi.org/project/MeanderAPI/#history"><img alt="PIPY Version" src="https://img.shields.io/pypi/v/MeanderAPI?style=for-the-badge&logo=python&color=65411d&logoColor=D9E0EE&labelColor=302D41"></a>
    <a href="https://pypi.org/project/MeanderAPI/"><img alt="PIPY Downloads" src="https://img.shields.io/pypi/dm/MeanderAPI?style=for-the-badge&logo=python&color=38427a&logoColor=D9E0EE&labelColor=302D41"></a>
    <br>
    <h3>Contributors</h3>
    <a href="https://github.com/elitrycraft/MeanderAPI/graphs/contributors">
        <img src="https://contrib.rocks/image?repo=elitrycraft/MeanderAPI" />
    </a>
</div>


## Features
### Here is what this library can do

- [x] Guest mode
- [x] Full Asynchrony
- [ ] Log-in to Accounts (DEVELOPING)




## Install
### Installation Process
You can easily install the library from PyPI using pip:

```bash
pip install MeanderAPI
```

## Quick start
### Getting Started with the Library

### Example 1
Getting a user info by id

```python
from MeanderAPI import GuestClient
import asyncio

async def main():
    async with GuestClient(__name__) as client:
        user = await client.getUserProfile(id="27ed560e-6a0f-4e67-bb7b-ce291e89f075")
        print(user)

asyncio.run(main())
```