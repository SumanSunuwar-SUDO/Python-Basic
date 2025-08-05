# using a while loop with lists and dictionaries
# Moving items from one list to another
unconfirmed__user = ['suman', 'anish', 'anuj']
confirmed_user = []

while unconfirmed__user:
    current_user = unconfirmed__user.pop()

    print("Verifying user: " + current_user.title())
    confirmed_user.append(current_user)

print("\nThe following user have been confirmed: ")
for user in confirmed_user:
    print(user.title())