# Hello Admin
username = ['admin', 'pele', 'messi', 'ronaldo', 'hanuman']
for user in username:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for log in again.")

# Checking username
current_users = ['admin', 'pele', 'messi', 'ronaldo', 'hanuman']
new_users = ['hanuman', 'Pele', 'neymar', 'iron man', 'superman']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " username has been already used.")
    else:
        print(new_user + " username is avaiable.")