import ollama

MODEL="llama2"

def ask(prompt:str)-> str:
    message=[{"role":"user","content": prompt}]
    response=ollama.chat(model=MODEL,messages=message)
    return response["message"]["content"]

if __name__== "__main__":
    print(ask("Explain what a token is in one sentence"))
    