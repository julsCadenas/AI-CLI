#!/usr/bin/env python3
import typer
import os
from menu import Menu
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("llama_url")
token = os.getenv("llama_token")

app = typer.Typer()
choice = Menu(url, token)

@app.command()
def meta():
    choice.meta()

@app.command()
def exit():
    choice.exit()

if __name__ == "__main__":
    app()