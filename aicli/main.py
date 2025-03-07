#!/usr/bin/env python3
import typer
import os
from aicli.menu import Menu
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
    change: bool = typer.Option(False, "--change", help="Suffix this to change the variables"),
    metaprompt: bool = typer.Option(False, "--metaprompt", help="Print the current prompt used by MetaAI"),
    metaheaders: bool = typer.Option(False, "--metaheaders", help="Print the current header used by MetaAI"),
    metaparams: bool = typer.Option(False, "--metaparams", help="Print the current parameters used by MetaAI"),
    metahistory: bool = typer.Option(False, "--metahistory", help="Print the path to the meta conversation history logs"),
    clear: bool = typer.Option(False, "--clear", help="Clears the history file")
):
    choice.settings_choices(username, change, metaprompt, metaheaders, metaparams, metahistory, clear)

@app.command()
def exit():
    choice.exit()

if __name__ == "__main__":
    app()
