while True:
    age_input = input("Enter your age (or 'quit' to exit): ")

    if age_input.lower() == 'quit':
        break

    age = int(age_input)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is Rs.1000.")
    else:
        print("Your ticket is Rs.1500.")
