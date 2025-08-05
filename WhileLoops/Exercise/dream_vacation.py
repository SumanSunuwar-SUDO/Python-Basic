places = {}
is_vacation = True

while is_vacation:
    name = input("Your name please:  ")
    response = input("If you could visit one place in the world, where would you go?  ")
    places[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/no)  ")
    if repeat.lower() == 'no':
        is_vacation = False
    
print("\n-- Poll Results --")
for name, place in places.items():
    print(name.title() + " would like to visit " + place.title() + ".")
