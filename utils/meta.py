import requests
from rich import print
from rich.syntax import Syntax
from rich.markdown import Markdown

class Meta_AI():
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.history = []
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.parameters = {
            "max_new_tokens": 5000,
            "temperature": 0.01,
            "top_k": 50,
            "top_p": 0.95,
            "return_full_text": False
        }
    
    def llm_query(self, query):
        context = "\n".join(self.history[-5:])
        # prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
        #     You are a helpful and smart assistant. You accurately provide answer to the provided user query.<|eot_id|>
        #     <|start_header_id|>user<|end_header_id|> 
        #     Here is the query: ```{query}```.
        #     Provide precise and concise answer.<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
        
        # prompt = f"""
        #     You are a helpful and smart assistant. You accurately provide answer to the provided user query.
        #     Here is the conversation history: {context}
        #     Here is the query: ```{query}```.
        #     Provide precise and concise answer.
        # """
        
        # prompt = f"""
        #     You are a helpful and smart assistant. Here is the conversation history: 
        #     {context}
        #     Now respond to the latest query: 
        #     ```{query}```.
        # """
        
        prompt = f"""
            You are a helpful and smart assistant. Here is the conversation history:
            {context}
            Now respond to the latest query as a human-like assistant, avoiding any meta-comments or prefixes:
            ```{query}```.
        """

        payload = {
            "inputs": prompt,
            "parameters": self.parameters
        }
        
        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            response_json = response.json()
            response_text = response_json[0]['generated_text'].strip()
            return response_text
        except KeyError as e:
            print(f"[bold red]KeyError: {e}[/bold red]")
            print(f"Response: {response.text}")
            return "Unexpected response format received from the server."
        except Exception as e:
            print(f"[bold red]An error occurred: {e}[/bold red]")
            return "An error occurred while fetching the response."

    def get_response(self, query, response):
        self.history.append(f"User: {query}")
        self.history.append(f"MetaAI: {response}")
        
        # print(f"[bold blue]You:[/bold blue] {query}")
        if '```' in response:
            parts = response.split('```')
            print(f"[bold red]MetaAI:[/bold red]", end="")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    md = Markdown(part.strip())
                    print(md)
                else:
                    lines = part.strip().split("\n", 1)
                    code = "\n".join(lines[1:]) if len(lines) > 1 else part.strip()
                    syntax = Syntax(code, "python", theme="dracula", line_numbers=True)
                    print(syntax)
        else:
            # md = Markdown(response.strip())
            print("[bold red]MetaAI:[/bold red] ", response.strip())
    
        