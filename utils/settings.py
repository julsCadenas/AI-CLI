from rich import print

class MetaSettings:
    def __init__(self, username="Gaylord"):
        self.username = username
    
    def update_username(self, new_username):
        self.username = new_username
        print(f"[bold yellow]Username updated to: {new_username}[/bold yellow]")
        return self.username

    