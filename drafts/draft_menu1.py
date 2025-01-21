#!/usr/bin/env python3
import typer
import os
from dotenv import load_dotenv
from utils.meta import Meta_AI
from rich import print
import sys

load_dotenv()

def main():
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
        
        # Get the response from MetaAI
        response = meta.llm_query(query)
        
        # Display and save the response
        meta.get_response(query, response)

if __name__ == "__main__":
    typer.run(main)
