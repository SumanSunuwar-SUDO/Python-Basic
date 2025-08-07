# Passing an Arbitary Number of Arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('muchrooms', 'green pappers', 'extra cheese')

# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with folowing toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')