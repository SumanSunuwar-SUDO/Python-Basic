dog = {'animal': 'Dog', 'owner': 'Chabi Lal'}
cat = {'animal': 'Cat', 'owner': 'Rajesh'}
parrot = {'animal': 'Parrot', 'owner': 'Akshya Kumar'}

pets = [dog, cat, parrot]

for pet in pets:
    print("\nPet Info:")
    for key, value in pet.items():
        print(key.title() + ": " + value)
