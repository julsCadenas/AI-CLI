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

url = os.getenv("llama_url")
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
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        # print(f"Response Status Code: {response.status_code}")
        # print(f"Response Text: {response.text}")
        # print(f"URL: {url}")
        # print(f"Token: {token[:5]}... (truncated for security)")
        response_json = response.json()
        response_text = response_json[0]['generated_text'].strip()
    except KeyError as e:
        response_text = "Unexpected response format received from the server."
        print(f"KeyError: {e}, Response: {response.text}")
    except Exception as e:
        response_text = f"An error occurred: {e}"


    return response_text

def main(query):
    response = llm(query)
    print(f"[bold blue]You:[/bold blue] {query}")
    if '```' in response:
        parts = response.split('```')
        print(f"[bold red]MetaAI:[/bold red]", end=" ")
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # print(part.strip())
                md = Markdown(part.strip())
                print(md)
            else:
                lines = part.strip().split("\n", 1)
                # language = lines[0] if len(lines) > 1 and lines[0] else "plaintext"
                code = "\n".join(lines[1:]) if len(lines) > 1 else part.strip()
                syntax = Syntax(code, "python", theme="dracula", line_numbers=True)
                print(syntax, "\n")
    else:
        md = Markdown(response.strip())
        print("[bold red]MetaAI:[/bold red]", end=" ")
        print(md, "\n") 
    

if __name__ == "__main__":
    typer.run(main)
    
