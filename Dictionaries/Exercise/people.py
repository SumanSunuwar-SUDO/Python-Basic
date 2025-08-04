person1 = {'first': 'Suman', 'last': 'Sunuwar', 'age': 20, 'city': 'Kathmandu'}
person2 = {'first': 'Gyanendra', 'last': 'Sahi', 'age': 22, 'city': 'Bhaktapur'}
person3 = {'first': 'Aman', 'last': 'Shrestha', 'age': 24, 'city': 'Kathmandu'}

people = [person1, person2, person3]

for person in people:
    print("\nPerson Info:")
    for key, value in person.items():
        print(key.title() + ": " + value)
