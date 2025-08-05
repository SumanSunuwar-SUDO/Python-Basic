# Using continue in a loop 
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding infinite Loops
x = 1
while x <= 5:
    print(x)
    x += 1
    # if you accidentally omit the line x += 1 (as shown next), 
    # the loop will run forever:
# This loop runs forever!
x = 1
while x <= 5:
 print(x)
 