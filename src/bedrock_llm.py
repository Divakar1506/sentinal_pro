import boto3
MODEL="us.amazon.nova-lite-v1:0"
client=boto3.client("bedrock-runtime",region_name="us-east-1")
def ask(prompt:str)-> str:
    messages=[{"role":"user","content":[{"text":prompt}]}]
    response=client.converse(
        modelId=MODEL,
        messages=messages,
        inferenceConfig={"maxTokens":100},
    )
    return response["output"]["message"]["content"][0]["text"]   
    
if __name__ =="__main__":
    print(ask("Explain what a token in one sentence"))
            