#!/usr/bin/env python3
import typer
import os
from dotenv import load_dotenv
from utils.meta import Meta_AI
load_dotenv()

# Store conversation history
conversation_history = []

def main(query: str):
    url = os.getenv("llama_url")
    token = os.getenv("llama_token")

    meta = Meta_AI(url, token)

    # Add query to history
    global conversation_history
    conversation_history.append(f"User: {query}")
    
    # Build conversational context
    context = "\n".join(conversation_history[-5:])  # Keep the last 5 interactions
    full_prompt = f"""
        You are a helpful and smart assistant. Engage in a friendly and conversational tone.
        Here is the conversation history:
        {context}
        Now respond to the latest query: ```{query}```.
        """
    response = meta.llm_query(full_prompt)

    # Save and display the assistant's response
    conversation_history.append(f"MetaAI: {response}")
    meta.get_response(query, response)

if __name__ == "__main__":
    typer.run(main)
