# passing arguments
# positional arguments

def describe_pet(animal_type, pet_name):
    '''Display the information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")

# multiple function calls
describe_pet("dog", "huskey")

# order matter in positional argument
describe_pet("harry", "hamster")

# Keyword arguments
describe_pet(animal_type="dog", pet_name="Billy")

# Default values
def describe_pet(pet_name, animal_type="dog"):
    '''display the information about a pet'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
describe_pet('jungey')

# Equivalent function calls
# -> A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# -> A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')