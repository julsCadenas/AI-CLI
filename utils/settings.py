from rich import print

class Settings():
    def __init__(self, query, context):
        self.parameters = {
            "max_new_tokens": 5000,
            "temperature": 0.01,
            "top_k": 50,
            "top_p": 0.95,
            "return_full_text": False
        }
        self.prompt = f"""
            You are a helpful and smart assistant. Here is the conversation history:
            {context}
            Now respond to the latest query as a human-like assistant, avoiding any meta-comments or prefixes:
            ```{query}```.
        """
        self.username = "Default user"
        self.prompt_templates = [
            f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are a helpful and smart assistant. You accurately provide answer to the provided user query.<|eot_id|>
            <|start_header_id|>user<|end_header_id|> 
            Here is the query: ```{query}```.
            Provide precise and concise answer.<|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            f"""
            You are a helpful and smart assistant. You accurately provide answer to the provided user query.
            Here is the conversation history: {context}
            Here is the query: ```{query}```.
            Provide precise and concise answer.
            """,
            f"""
            You are a helpful and smart assistant. Here is the conversation history: 
            {context}
            Now respond to the latest query: 
            ```{query}```.
            """,
            f"""
            You are a helpful and smart assistant. Here is the conversation history:
            {context}
            Now respond to the latest query as a human-like assistant, avoiding any meta-comments or prefixes:
            ```{query}```.
            """
        ]
        
    def set_username(self):
        username = input("Enter your username: ")
        self.username = username
        print(f"[bold green]Username set to: {username}[bold green]")
    
    def get_username(self):
        return self.username
    
    def set_meta_parameters(self):
        self.parameters = {
            "max_new_tokens": 5000,
            "temperature": 0.01,
            "top_k": 50,
            "top_p": 0.95,
            "return_full_text": False
        }
        print(f"[bold]Current Parameters:[bold] {self.parameters}")
        print("[bold green]Edit Meta AI Parameters.[bold green]")
        self.parameters["max_new_tokens"] = input("Enter max_new_tokens: ")
        self.parameters["temperature"] = input("Enter temperature: ")
        self.parameters["top_k"] = input("Enter top_k: ")
        self.parameters["top_p"] = input("Enter top_p: ")
        self.parameters["return_full_text"] = input("Return full text? [True/False]: ")
    
    def get_meta_parameters(self):
        return self.parameters
    
    def set_meta_prompt(self, prompt):
        print(f"[bold]Current Prompt:[bold] {self.prompt}")
        print("[bold green]Choose a template prompt or write your own?:[y/n][bold green] ", end="")
        choice = input()
        if choice.lower() == "y":
            print("[bold green]Choose a template prompt:[bold green]")
            for i in self.prompt_templates:
                print(i)
            
        elif choice.lower() == "n":
            print ("[bold blue]Enter your prompt for the Meta AI:[bold blue] ")
            prompt = input()
        self.prompt = prompt
        print(f"[bold green]Prompt set to: {prompt}[bold green]")
    
    def restore_to_default(self):
        self.parameters = {
            "max_new_tokens": 5000,
            "temperature": 0.01,
            "top_k": 50,
            "top_p": 0.95,
            "return_full_text": False
        }
        self.prompt = """
            You are a helpful and smart assistant. Here is the conversation history:
            {context}
            Now respond to the latest query as a human-like assistant, avoiding any meta-comments or prefixes:
            ```{query}```.
        """
        self.username = "Default user"

        print("[bold green]Settings restored to default.[bold green]")
    
    def get_meta_prompt(self):
        return self.prompt