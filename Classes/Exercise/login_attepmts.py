class User():
    def __init__(self, first_name, last_name, email, username, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.username = username
        self.age = age
        self.login_attempts = 0

    def descibe_user(self):
        full_name = self.first + " " + self.last
        print("\nName: " + full_name.title())
        print("Email: " + self.email)
        print("Username: " + self.username)
        print("Age: " + str(self.age))
    
    def greet_user(self):
        full_name = self.first + " " + self.last
        print("Hello, " + full_name.title() + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
# instances
user1 = User('suman', 'sunuwar', 'suman@gmail.com', 'suman123', 22)
user2 = User('anuj', 'bhattarai', 'anuj@gmail.com', 'anum123', 20)

# calling methods
user1.descibe_user()
user1.greet_user()
user2.descibe_user()
user2.greet_user()

# login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print('Login attempts for ' + user1.username + ": " + str(user1.login_attempts))
user1.reset_login_attempts()
print("After Reset: " + str(user1.login_attempts))