players = ['Pele', 'Neymar', 'Messi', 'Rondaldo']
print(players)

# Accessing Elements in a List
print(players[1])
print(players[1].upper())

# Index Positions Start at 0, Not 1
print(players[0])

# the item at index -1, Python always returns the last item in the list:
print(players[-1])

# Using individual values from a list

message = " His name is " + players[3].title() + "."
print(message)

# Changing, Adding, and Removing Elements
# Modifying Elements in a List
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)
motorcyles[0] = "ducati"
print(motorcyles)

# Adding elements to a list
# Appending
motorcyles.append("honda")
print(motorcyles)

# Inserting
motorcyles.insert(1, "honda")
print(motorcyles)

# Removig Elements from a List
# using the del statement
del motorcyles[1]
print(motorcyles)

# using the pop() method
popped_motorcycle = motorcyles.pop(2)
print(motorcyles)
print(popped_motorcycle)

# removing an item by value
motorcyles.remove('yamaha')
print(motorcyles)

# Organizing a list
motorcyles.sort()
print(motorcyles)
motorcyles.reverse()
print(motorcyles)
print(len(motorcyles))