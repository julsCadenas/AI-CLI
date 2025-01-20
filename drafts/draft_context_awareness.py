#!/usr/bin/env python3
import typer
import os
from dotenv import load_dotenv
from utils.meta import Meta_AI

load_dotenv() 

def main():
    url = os.getenv("llama_url")
    token = os.getenv("llama_token")
    meta = Meta_AI(url, token)

    conversation_history = []

    print("[bold green]Welcome to MetaAI! Start your conversation below. Type 'exit' to end the session.[/bold green]\n")

    while True:
        query = input("[bold blue]You:[/bold blue] ")
        if query.lower() == "exit":
            print("[bold green]Goodbye! Have a great day![/bold green]")
            break
        
        # Include the conversation history in the prompt
        conversation = "\n".join([f"You: {q}\nMetaAI: {r}" for q, r in conversation_history])
        full_prompt = f"{conversation}\nYou: {query}\nMetaAI:"
        
        # Fetch response
        response = meta.llm_query(full_prompt)
        
        # Display response
        meta.get_response(query, response)
        
        # Update conversation history
        conversation_history.append((query, response))

if __name__ == "__main__":
    typer.run(main)
