import json
from types import FunctionType


def run_llama(input_str):
    from ollama import Client

    client = Client()
    result = client.generate(model="llama3.2:latest", prompt=input_str)
    return result["response"]


input_str = "why is sky blue?"
result = run_llama(input_str)
print(result)
