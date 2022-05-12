prompt = "\nTell me something, and I will repeat it beck to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(prompt)