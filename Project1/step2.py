import requests

url = "http://localhost:11434/api/chat"

messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
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
