animals = ['cat', 'dog', 'rabbit', 'hamster']

# equality check
if animals == 'cat':
    print("It's a cat.")
else:
    print("It's not a cat.")

# inequality check
if animals != 'dog':
    print("It's not a dog.")
else:
    print("It's a dog.")

# Tests using the lower() function
name = 'Neymar'
print(name.lower() == 'neymar')
print(name.lower() == 'pele') 

# Numerical tests
x = 10
y = 5
print(x == 10)
print(x != y)
print(x > y)
print(x < y)
print(x >= 10)
print(y <= 3)

# Tests using and / or
age = 20
print(age > 18 and age < 25)
print(age < 18 and age < 25)
print(age < 18 or age < 25)
print(age > 25 or age < 18)

# Test whether an item is in a list
animals = ['cat', 'dog', 'rabbit']
print('cat' in animals)
print('lion' in animals)

# Test whether an item is not in a list
print('lion' not in animals)
print('dog' not in animals)
