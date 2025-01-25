import sys
from rich import print
from utils.meta import Meta_AI
from utils.settings import MetaSettings

class Menu:
    def __init__(self, url, token):
        self.url = url
        self.token = token
    
    def exit(self):  
        print("[bold cyan]Goodbye![/bold cyan]")
        sys.exit(0)

    def meta(self):  
        url = self.url
        token = self.token
        
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