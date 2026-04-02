import os
from ollama import Client
from traceloop.sdk import Traceloop

Traceloop.init(app_name="ollama-chat", disable_batch=True)

MODEL_NAME = os.getenv("LLM_MODEL", "llama3.2:1b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

client = Client(host=OLLAMA_HOST)

def chat():
    print(f"\n--- CLI Chat con il modello: {MODEL_NAME} ---")
    while True:
        user_input = input("\nTu > ")
        if user_input.lower() in ["exit", "quit", "esci"]:
            break
            
        response = client.generate(model=MODEL_NAME, prompt=user_input)
        print(f"\nOllama ({MODEL_NAME}) > {response['response']}")

if __name__ == "__main__":
    chat()
