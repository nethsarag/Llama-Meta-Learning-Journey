import requests
import json

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Say hello in one sentence."}
    ],
    "stream": False
}

response = requests.post(url, json=payload)
data = response.json()

print(data["message"]["content"])