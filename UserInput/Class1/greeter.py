# How the input() function works
name = input("Your Name: ")
print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, " + name + "!")

# using int() to accept numerical input
age = int(input("How old are you?\t"))
print(age)