# The while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# let the user choose when to quit
prompt = "Enter your message: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using Flag
active = True

while active:
    message = input(prompt)

    if message == "quit" :
        active = False
    else:
        print(message)