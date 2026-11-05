
import ollama
messages = [{"role":"assistent", "content":"You are friendly assistent."}]
model_name = "llama3.2:latest"
while True:
    user_prompt = input("You: ")
    if user_prompt=="bye":
        break
    user_role = {"role":"user", "content":user_prompt}
    messages.append(user_role)

    response = ollama.chat(model = model_name, messages=messages)
    response = response.message.content
    print("Assistent: ", response)
    assistent_role = [{"role":"assistent", "content":response}]
    messages.append(assistent_role)


