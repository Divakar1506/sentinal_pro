from src.validator import validate_req
import ollama

def handle(req:str)-> str:
    clean= validate_req(req)
    request=ollama.chat(model=clean["model"],messages=clean["messages"],options={"num_predict":clean["max_tokens"]})
    return request["message"]["content"]

if __name__ == "__main__":
        good={"model":"llama2","messages":[{"role":"user","content":"What is Rag in one sentence"}],"max_tokens":100}
        bad={"model":"gpt-5","messages":[{"role":"user","content":"hi"}],"max_tokens":100}
for req in [good,bad]:
    try:
        print(handle(req))
    except ValueError as e:
        print("Rejected:",e)