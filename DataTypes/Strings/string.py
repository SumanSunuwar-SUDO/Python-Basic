message = "This is a string variable."
print(message)

# changing case of the string
print(message.title())  # Title case
print(message.lower())  # Lowercase
print(message.upper())  # Uppercase

#Combining or Concatinating strings
first_name = "Neymar"
last_name = "Junior"
full_name = first_name + " " + last_name
print(full_name)
message = " Hello, " + full_name.title() + "!"
print(message)

# Stripping whitespace
favourite_language = " python "
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

# avoiding syntax error with strings
message = "One of python's strength is its diverse community."
print(message)