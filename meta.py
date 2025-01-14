#!/usr/bin/env python3

'''
TO DO:
- add history
- make it fully conversational
- make it automated

'''

import requests
import os
import typer
from rich import print
from rich.syntax import Syntax
from rich.markdown import Markdown
from dotenv import load_dotenv
load_dotenv()

url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
token = os.getenv("llama_token")

def llm(query):
    parameters = {
        "max_new_tokens": 5000,
        "temperature": 0.01,
        "top_k": 50,
        "top_p": 0.95,
        "return_full_text": False
        }
    
    prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>You are a helpful and smart assistant. You accurately provide answer to the provided user query.<|eot_id|><|start_header_id|>user<|end_header_id|> Here is the query: ```{query}```.
        Provide precise and concise answer.<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    prompt = prompt.replace("{query}", query)
    
    payload = {
        "inputs": prompt,
        "parameters": parameters
    }
  
    response = requests.post(url, headers=headers, json=payload)
    response_text = response.json()[0]['generated_text'].strip()

    return response_text

def main(query):
    response = llm(query)
    print(f"[bold blue]You:[/bold blue] {query}")
    if '```' in response:
        parts = response.split('```')
        # formatted_response = []
        print(f"[bold red]MetaAI:[/bold red]", end=" ")
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # print(part.strip())
                md = Markdown(part.strip())
                print(md)
                # formatted_response.append(part.strip())
            else:
                lines = part.strip().split("\n", 1)
                # language = lines[0] if len(lines) > 1 and lines[0] else "plaintext"
                code = "\n".join(lines[1:]) if len(lines) > 1 else part.strip()
                syntax = Syntax(code, "python", theme="dracula", line_numbers=True)
                print(syntax, "\n")
    else:
        print(f"[bold red]MetaAI:[/bold red] {response} \n")
    

if __name__ == "__main__":
    typer.run(main)