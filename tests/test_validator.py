import pytest
from src.validator import validate_req

def test_validate_request_passes():
    req={"model":"llama2","messages":[{"role":"user","content":"hi"}],"max_tokens":100}
    result=validate_req(req)
    assert result["max_tokens"]==100
    
def test_unknown_model_rejected():
    req={"model":"gpt5","messages":[{"role":"user","content":"hi"}],"max_tokens":100} 
    with pytest.raises(ValueError):
        validate_req(req) 
 
def test_empty_messages_rejected():
    req={"model":"llama2","messages": [],"max_tokens":100}
    with pytest.raises(ValueError):
        validate_req(req)             

def test_missing_max_tokens_rejected():
    req={"model":"llama2","messages": [{"role":"user","content":"hi"}]}
    with pytest.raises(ValueError):
        validate_req(req)
 
 
def test_string_messages_rejected():
    req={"model":"llama2","messages":"hello","max_tokens":100}
    with pytest.raises(ValueError):
        validate_req(req)
    
                    
def test_bool_tokens_rejected():
    req={"model":"llama2","messages":[{"role":"user","content":"hi"}],"max_tokens":True}
    with pytest.raises(ValueError):
        validate_req(req)
                        
                        
def test_out_of_range_tokens_rejected():
    req={"model":"llama2","messages":[{"role":"user","content":"hi"}],"max_tokens":5000}
    with pytest.raises(ValueError):
        validate_req(req)                           