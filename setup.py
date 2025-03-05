from setuptools import setup, find_packages

setup(
    name="aicli",  
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "aicli=aicli.main:app",  
        ]
    }
)
