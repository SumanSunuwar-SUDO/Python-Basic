# defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# passing information to a function
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user("Suman")