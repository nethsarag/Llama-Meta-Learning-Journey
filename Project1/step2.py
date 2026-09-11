import requests
import json

url = "http://localhost:11434/api/chat"

messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        with open("conversation.json", "w") as f:
            json.dump(messages, f, indent=2)
        print("Conversation has been saved at conversation.json")
        break
    

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "llama3.2",
        "messages": messages,
        "stream": False
    }
    response = requests.post(url, json=payload)
    data = response.json()
    reply = data["message"]["content"]

    print("Llama", reply)

    messages.append({"role": "assistant", "content": reply})
