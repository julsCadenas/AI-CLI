import requests
from rich import print
from rich.syntax import Syntax
from rich.markdown import Markdown
from utils.settings import Settings

class Meta_AI():
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.history = []
        self.settings = Settings()
        self.username = self.settings.load_username()
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }

    def llm_query(self, query):
        context = "\n".join(self.history[-5:])
        username = self.username
        
        parameters = {
            "max_new_tokens": 5000,
            "temperature": 0.01,
            "top_k": 50,
            "top_p": 0.95,
            "return_full_text": False
        }
        
        prompt = self.settings.load_prompt().format(username=username, context=context, query=query)
        # prompt = f"""You are a helpful and smart assistant. You accurately provide answers to user queries while maintaining context.
        #         The user's name is {username}.
        #         Here is the conversation history: {context}
        #         Now, respond to the latest query in a precise and concise manner: ```{query}```.
        # """
         
                    
        payload = {
            "inputs": prompt,
            "parameters": parameters,
            # "add_generation_prompt": True 
        }
       
        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            response_json = response.json()
            response_text = response_json[0]['generated_text'].strip()
            return response_text
        except KeyError as e:
            print(f"[bold red]KeyError: {e}[/bold red]")
            print(f"[bold red]Response:[bold red] {response.text}")
            return "Unexpected response format received from the server."
        except Exception as e:
            print(f"[bold red]An error occurred: {e}[/bold red]")
            return "An error occurred while fetching the response."

    def get_response(self, query, response):
        self.history.append(f"User: {query}")
        self.history.append(f"MetaAI: {response}")
       
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
            print("[bold red]MetaAI:[/bold red] ", response.strip())