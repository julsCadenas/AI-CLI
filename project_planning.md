# AICLI
## Integrating LLMs on your terminal

### Features
- Integrate LLAMA (Meta AI) in the terminal **DONE**
- Integrate ChatGPT (OpenAI) in the terminal **UNSURE SINCE THIS IS PAID**
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
- fix llama prompt 
- make meta ai fully conversational **DONE**
- make meta ai have context awareness **DONE**
- make settings class/function **DONE** 
- add loading/progress indicators **DONE**
- make the terminal capable of accepting multiline inputs and pasted inputs
- fix keyboard controls in terminal when using app

### Notes
- type ```meta``` in the terminal and will activate the llama chatbot in the terminal
- type ```manai <command>``` 
- try your best to implement an autocomplete feature