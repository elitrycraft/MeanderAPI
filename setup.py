from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MeanderAPI",
    version="0.1.6",
    author="Deniz1111212",
    author_email="elitrycraft@gmail.com",
    maintainer="CodCatDev",
    maintainer_email="codcatdev@gmail.com",
    description="A python library for interact with Meander API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elitrycraft/MeanderAPI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords="meander api wrapper quests",
    project_urls={
        "Bug Reports": "https://github.com/elitrycraft/MeanderAPI/issues",
        "Source": "https://github.com/elitrycraft/MeanderAPI",
    },
)
