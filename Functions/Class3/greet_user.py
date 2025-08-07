# passing a list 
def greet_user(names):
    ''' Print a simple greeting to each user in the list.'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['suman', 'anuj', 'anish', 'pasang']
greet_user((usernames))