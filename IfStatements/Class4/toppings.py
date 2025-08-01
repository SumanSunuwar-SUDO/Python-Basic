
# Using if Statements with Lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished naking your pizza.")


# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# Using Multiple Lists
avaiable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french pries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza.")


# Styling Your if Statement

'''
if age < 4:

is better than:

if age<4:
'''

# Such spacing does not affect the way Python interprets your code;
# it just makes your code easier for you and others to read.