# when you write the class,
# you define the general behaviour that a whole category of objects can have


# Creating and Using a Class
"""
class ClassName(object):
 --snip--
"""
class Dog():
    '''a simple attempt to model a dog'''

    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(self.name.title() + " rolled over!")


# Making an Instance from a Class
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ". ")
print("My dog is " + str(my_dog.age) + "years old. ")

# accessing attributes
my_dog.name

# calling methods
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("Your dog's name is " + your_dog.name.title() + ".")