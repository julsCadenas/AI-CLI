from rich import print
import json
import os

class Settings:
    def __init__(self):
        self.settings_file = os.path.join(os.path.dirname(__file__), "..", "settings.json")
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
    
    def load_meta_prompt(self):
        if self.settings:
            return self.settings.get("meta_prompt", "Default prompt template not found.")
        else:
            print("[bold red]Settings not loaded properly![/bold red]")
            return None
        
    def load_meta_headers(self):
        if self.settings:
            return self.settings.get("meta_headers", {})
        else:
            print("[bold red]Settings not loaded properly![/bold red]")
            return None
        
    def load_meta_parameters(self):
        if self.settings:
            return self.settings.get("parameters", {})
        else:
            print("[bold red]Settings not loaded properly![/bold red]")
            return None
    
    def handle_change(self, key: str, is_dict=False):
        print(f"[bold yellow]Current {key}:[/bold yellow] {self.settings.get(key, 'Not Set')}")
        print(f"[bold blue]Input new value for {key}:[/bold blue] ", end="")
        new_value = input()

        if new_value:
            if is_dict:
                try:
                    new_value = json.loads(new_value)  
                except json.JSONDecodeError:
                    print("[bold red]Invalid JSON format![/bold red]")
                    return
            self.settings[key] = new_value
            self.save_settings()
            print(f"[bold green]{key} updated successfully![/bold green]")
        else:
            print(f"[bold red]{key} cannot be empty![/bold red]")
    
    def get_setting(self, key: str):
        return self.settings.get(key, "Not Set")
    
    def clear_history(self):
        try:
            with open(self.settings["meta_history_path"], "w") as file:
                file.write("")
            print("[bold green]History cleared successfully![/bold green]")
        except Exception as e:
            print(f"[bold red]An error occurred while clearing history: {e}[/bold red]")
        