# returning a simple value
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = first_name + " " + last_name
    return full_name.title()

footballer = get_formatted_name("neymar", 'junior')
print(footballer)

# making an argument optional
def formatted_name(first_name, last_name,  middle_name='' ):
    '''Return a full name, neatly formatted'''
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()

person = formatted_name("Suman" , "Sunuwar")
print(person)