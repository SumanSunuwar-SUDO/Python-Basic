# looping through entire list
# for item in list_of_items
magicians = ['alice', 'david', 'bob', 'carolina']
for magician in magicians:
    print(magician)

# Making Numerical List
# using the range() Function

for value in range(1, 5):
    print(value)

# using range() to make a list of numbers

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    # squares.append(value**2)
print(squares)

# simple statistics with a list of numbers
digits = list(range(1, 10))
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squares = [ value**2 for value in range(1, 11)]
print(squares)

# Slicing a list
fruits = ['apple', 'banana', 'mango', 'orange', 'grapes']
print(fruits[0:2])
print(fruits[1:3])
print(fruits[:4])
print(fruits[2:])

# looping through  a Slice
for fruit in fruits[:4]:
    print(fruit.title())

# Copying a List
copy_of_fruits = fruits[:]
print(copy_of_fruits)

