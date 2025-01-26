import sys
from rich import print
from utils.meta import Meta_AI
from utils.settings import Settings

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
    
    def settings_choices(self, username: bool, change: bool, metaprompt: bool, metaheaders: bool, metaparams: bool):
            settings_manager = Settings()
            
            if username:
                if change:
                    settings_manager.handle_change("username")
                else:
                    print(f"[bold yellow]Current username:[/bold yellow] {settings_manager.get_setting('username')}")
            
            if metaprompt:
                if change:
                    settings_manager.handle_change("meta_prompt")
                else:
                    print(f"[bold yellow]Current meta prompt:[/bold yellow] {settings_manager.get_setting('meta_prompt')}")

            if metaheaders:
                if change:
                    settings_manager.handle_change("meta_headers", is_dict=True)
                else:
                    print(f"[bold yellow]Current meta headers:[/bold yellow] {settings_manager.get_setting('meta_headers')}")

            if metaparams:
                if change:
                    settings_manager.handle_change("parameters", is_dict=True)
                else:
                    print(f"[bold yellow]Current meta parameters:[/bold yellow] {settings_manager.get_setting('parameters')}")
                
