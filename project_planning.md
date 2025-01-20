# AICLI
## Integrating LLMs on your terminal

### Features
- Integrate LLAMA (Meta AI) in the terminal **DONE**
- Integrate ChatGPT (OpenAI) in the terminal
- Try to add an autocomplete feature within the terminal using available AI/ML tools
- Try to add add an AI version of the linux ```man``` command

### Folder Structure
- `root/`
    - `.venv/`
    - `main.py`
    - `.env`
    - `.gitignore`
    - `requirements.txt`
    - `utils/`
        - `__pycache__/`
        - `meta.py`
        - `autocomplete.py`
        - `ai_man.py`
    - `drafts/`
        - `draft_codes.py`

## TO DO LIST
- make meta ai fully conversational
- make meta ai have context awareness
- make the terminal capable of accepting multiline inputs and pasted inputs

### Notes
- type ```meta``` in the terminal and will activate the llama chatbot in the terminal
- type ```manai <command>``` 
- type ```gpt``` in the terminal to call and activate thye chatgpt/openai chatbot in the terminal
- try your best to implement an autocomplete feature