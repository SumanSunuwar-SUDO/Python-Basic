class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome to our " + self.name.title() + "!" + 
              "\nOur restaurant serves " + self.type.title())

    def open_restaurant(self):
        print(self.name.title() + " is open at 7:00AM.")
    
    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative!")

    def increment_number_served(self, increment):
        if increment > 0:
            self.number_served += increment
        else:
            print("Increment must be positive!")

# Creating an instance
restaurant = Restaurant("Gokarna Hillside Restaurant", "Nepali and continental")

# Printing attributes individually
print("Restaurant Name:", restaurant.name)
print("Cuisine Type:", restaurant.type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Change number served directly
restaurant.number_served = 20
print("Number served after direct change:", restaurant.number_served)

# Use method to set number served
restaurant.set_number_served(50)
print("Number served after set_number_served():", restaurant.number_served)

# Increment number served
restaurant.increment_number_served(30)
print("Number served after increment_number_served():", restaurant.number_served)