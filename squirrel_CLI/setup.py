from setuptools import setup
 
 
version = "0.0.1"

description="Set up your workflow environment with Squirrel"
 
setup(
    name = "squirrel",
    packages = ["squirrel","squirrel.commonf"],
    entry_points = {
        "console_scripts": ['sq = squirrel.sqrl:main']
        },
    version = version,
    description = "Command line app for setting up your working environment",
    long_description = description,
    author = "Pavel B. Zegarra",
    author_email = "pavelbrn@gmail.com",
    url = "http://github.com/pavelbrn",
    )