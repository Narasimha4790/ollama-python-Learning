import ollama


messages=[]

print("welcome, type 'exit' to stop the conversation")

while True:

    user_input=input("You:")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role":"user",
        "content":user_input
    }) 

    response=ollama.chat(
        model="llama3.2",
        messages=messages
    )

    assistant_reply=response.message.content

    print("assistant:",assistant_reply)

    messages.append({
        "role":"assistant",
        "content":assistant_reply
    })