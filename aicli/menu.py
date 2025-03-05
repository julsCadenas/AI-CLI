import sys
from rich import print
from aicli.utils.meta import Meta_AI
from aicli.utils.settings import Settings
from aicli.utils.helpers import Helpers

class Menu:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.mode = "normal"
    
    def exit(self):  
        print("[bold cyan]Goodbye![/bold cyan]")
        sys.exit(0)

    def meta(self):  
        url = self.url
        token = self.token
        mode = self.mode
        
        if not url or not token:
            print("[bold red]Error: Missing URL or token from environment variables[/bold red]")
            sys.exit(1)

        meta = Meta_AI(url, token)
        
        print("[bold green]Welcome to the MetaAI chatbot! Type '/exit' to end the conversation.[/bold green]")
        print(f"[bold yellow]You are currently on {mode.capitalize()} Mode. Type '/mode' to switch [/bold yellow]")
        # mode = input()
        
        # print(f"[bold magenta]You are now in {mode.capitalize()} Mode. Type '/mode' to switch modes at any time.[/bold magenta]")
        # print("[bold green]Type 'exit' to end the conversation.[/bold green]")
        
        while True:
            print(f"[bold blue]({mode.capitalize()} Mode) You:[/bold blue]", end=" ")
            
            if mode == "multiline":
                query = Helpers.multiline_input()
            else:
                query = input().strip()
            
            if query.lower() == "/exit":
                print("\n[bold green]Goodbye! Have a great day![/bold green]")
                break
            
            if query.lower() == "/mode":
                mode = "multiline" if mode == "normal" else "normal"
                print(f"\n[bold magenta]Switched to {mode.capitalize()} Mode.[/bold magenta]")
                continue
            
            response = meta.llm_query(query)
            meta.get_response(query, response)
    
    def settings_choices(self, username: bool, change: bool, metaprompt: bool, metaheaders: bool, metaparams: bool, metahistory: bool, clear: bool):
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
                
            if metahistory:
                if change:
                    settings_manager.handle_change("meta_history_path")
                if clear:
                    settings_manager.clear_history()
                else:
                    print(f"[bold yellow]Current meta history path:[/bold yellow] {settings_manager.get_setting('meta_history_path')}")