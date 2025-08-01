# if statements
age = 19
if age >= 18:
    print("You are eligible to vote.")

# if-else statement
age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# if-elif-else statement
age = 20
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# using multiple elif blocks
age = 12
if age < 4:
    price = "Free"
elif age < 18:
    price = "Rs.1000"
elif age < 65:
    price = "Rs.2000"
else:
    price = "Rs.1500"

print("Your ticket price is:" + price + ".")