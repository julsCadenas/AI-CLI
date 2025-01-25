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
def settings(
    username: bool = typer.Option(False, "--username", help="Print current username"),
    change: bool = typer.Option(False, "--change", help="Change the username"),
    metaprompt: bool = typer.Option(False, "--metaprompt", help="Print the current prompt used by MetaAI")
):
    choice.settings_choices(username, change, metaprompt)

@app.command()
def exit():
    choice.exit()

if __name__ == "__main__":
    app()
