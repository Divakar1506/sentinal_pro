Allowed_models={"claude-haiku","claude-opus","claude-sonnet"}
def validate_req(req):
    model=validate_model(req["model"])
    message=validate_message(req['messages'])
    tokens=validate_tokens(req.get("max_tokens"))
    
    
    return {'model':model,'messages':message,'max_tokens':tokens}    

def validate_model(model):
    if model not in Allowed_models:
        raise ValueError("Model not found")
    return model
def validate_message(message):
    if not isinstance(message,list):
        raise ValueError("Error data type")
    if len(message)==0:
        raise ValueError("Message shouldn't be empty")
    return message

def validate_tokens(tokens):
    if tokens is None:
        raise ValueError("max_token is required")
    if  isinstance(tokens,bool):
        raise ValueError("Tokens shouldnot be bool")
    if not isinstance(tokens,int):
        raise ValueError("Tokens should be an integer")
    if tokens <=0 or tokens >4096:
        raise ValueError("Invalid tokens")
    return tokens
     


if __name__=="__main__":
    tests = [
        {"model": "claude-haiku", "messages": [{"role": "user", "content": "hi"}], "max_tokens": 512},
        {"model": "gpt-5",        "messages": [{"role": "user", "content": "hi"}], "max_tokens": 512},
        {"model": "claude-haiku", "messages": [],                                  "max_tokens": 512},
        {"model": "claude-haiku", "messages": [{"role": "user", "content": "hi"}]},
        {"model": "claude-haiku", "messages": "hello",                             "max_tokens": 512},
        {"model": "claude-haiku", "messages": [{"role": "user", "content": "hi"}], "max_tokens": True},
        {"model": "claude-haiku", "messages": [{"role": "user", "content": "hi"}], "max_tokens": ""}
    ]
    for req in tests:
        try:
            print(validate_req(req))
        except ValueError as e:
            print("Rejected: ",e)