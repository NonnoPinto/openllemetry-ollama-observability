import os
from ollama import Client
from traceloop.sdk import Traceloop

Traceloop.init(app_name="ollama-chat", disable_batch=True)

client = Client(host=os.getenv("OLLAMA_HOST", "http://ollama:11434"))

def chat():
    print("--- CLI Chat con Ollama & Traceloop Cloud ---")
    while True:
        user_input = input("\nTu > ")
        if user_input.lower() in ["exit", "quit", "esci"]:
            break
            
        # Questa chiamata viene intercettata AUTOMATICAMENTE
        response = client.generate(model='llama3.2:1b', prompt=user_input)
        
        print(f"\nOllama > {response['response']}")

if __name__ == "__main__":
    chat()
