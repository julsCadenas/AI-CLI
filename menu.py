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
    
    def settings(self):
        settings = Settings(query=None, context=None)
        print("[bold green]Settings:[bold green]")
        print("[bold green]1. Set Username[bold green]")
        print("[bold green]2. Set Meta AI Parameters[bold green]")
        print("[bold green]3. Set Meta AI Prompt[bold green]")
        print("[bold green]4. Restore to Default[bold green]")
        print("[bold green]5. Exit[bold green]")
        print("[bold green]Choose an option:[bold green] ", end="")
        choice = input()
        
        if choice == "1":
            settings.set_username()
        elif choice == "2":
            settings.set_meta_parameters()
        elif choice == "3":
            settings.set_meta_prompt()
        elif choice == "4":
            settings.restore_to_default()
        elif choice == "5":
            self.exit()
        else:
            print("[bold red]Invalid choice. Please try again.[bold red]")
            self.settings()