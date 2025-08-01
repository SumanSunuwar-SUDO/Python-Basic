# Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical Comparisons
age = 18
print(age == 18)

answer = 17
if answer !=  20:
    print("That is not the correct answer. Please try again.")

# Checking multiple conditions
    # using and to check multiple conditions
age_0 = 20
age_1 = 21
print(age_0 >= 20 and age_1 >= 100)
print(age_0 >= 20 and age_1 >= 21)

# using or to check multiple conditions
print(age_0 >= 20 or age_1 >= 100)
print(age_0 >= 100 or age_1 >= 100)

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#Boolean Expressions
game_active = True
can_edit = False
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')