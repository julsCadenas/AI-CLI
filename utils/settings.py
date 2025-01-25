from rich import print
import json

class Settings:
    def __init__(self, settings_file = "settings.json"):
        self.settings_file = settings_file
        self.settings = self.load_settings()
    
    def load_settings(self):
        try:
            with open(self.settings_file, "r") as file:
                settings_data = json.load(file)
                return settings_data
        except FileNotFoundError:
            print("[bold red]Settings file not found![/bold red]")
            return None
        except json.JSONDecodeError:
            print("[bold red]Error decoding JSON from settings file![/bold red]")
            return None
    
    def save_settings(self):
        try:
            with open(self.settings_file, "w") as file:
                json.dump(self.settings, file, indent=4)
        except Exception as e:
            print(f"[bold red]An error occurred while saving settings: {e}[/bold red]")
        
    def load_username(self):
        if self.settings:
            return self.settings["username"]
        else:
            print("[bold red]Username not found![/bold red]")
            return None
    
    def handle_username_change(self, username: bool, change: bool):
        if username and not change:
            print(f"[bold yellow]Current username:[/bold yellow] {self.load_username()}")
        elif username and change:
            print("[bold blue]Input new username:[/bold blue] ", end="")
            new_username = input()
            if new_username:
                self.settings["username"] = new_username
                self.save_settings()
            else:
                print("[bold red]Username cannot be empty![/bold red]")
        else:
            print("[bold red]settings --username --change[/bold red] to update.")

    def load_meta_prompt(self):
        if self.settings:
            return self.settings.get("meta_prompt", "Default prompt template not found.")
        else:
            print("[bold red]Settings not loaded properly![/bold red]")
            return None
    
    def load_meta_parameters(self):
        if self.settings:
            return self.settings.get("parameters", {})
        else:
            print("[bold red]Settings not loaded properly![/bold red]")
            return None