#!/usr/bin/env python3
import typer
import os
from dotenv import load_dotenv
from utils.meta import Meta_AI
from rich import print
import sys

load_dotenv()
app = typer.Typer()

@app.command()
def meta():
    url = os.getenv("llama_url")
    token = os.getenv("llama_token")
    
    if not url or not token:
        print("[bold red]Error: Missing URL or token from environment variables[/bold red]")
        sys.exit(1)

    meta = Meta_AI(url, token)
    
    print("[bold green]Welcome to the MetaAI chatbot! Type 'exit' to end the conversation.[/bold green]")
    
    while True:
        print("[bold blue]You:[/bold blue]", end=" ")
        query = input()
        
        if query.lower() == "exit":
            print("[bold green]Goodbye! Have a great day![/bold green]")
            break
        
        response = meta.llm_query(query)
        
        meta.get_response(query, response)

@app.command()
def exit():
    print("[bold cyan]Goodbye![/bold cyan]")
    sys.exit(0)

if __name__ == "__main__":
    app()
