"""prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)"""

        #need to understand
active = True
while active:
    message = input("put something or quit: ")
    if message == "quit":
        active = False
    else:
        print(message)
