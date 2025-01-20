#!/usr/bin/env python3
import typer
import os
from dotenv import load_dotenv
from utils.meta import Meta_AI
load_dotenv() 

def main(query):
    url = os.getenv("llama_url")
    token = os.getenv("llama_token")

    meta = Meta_AI(url, token)
    response = meta.llm_query(query)
    meta.get_response(query, response)

if __name__ == "__main__":
    typer.run(main)
    