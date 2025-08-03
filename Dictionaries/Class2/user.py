# Looping through  all key-value pairs
user = {
    'username' : 'Suman',
    'first' : 'suman',
    'last' : 'sunuwar',
}

for key, value in user.items():
    print("\nKey :" + key)
    print("\nValue :"  + value)

# Looping through all the keys in a dictionary
for key in user.keys():
    print(key.title())

favourite_languages = {
    'anuj' : 'c',
    'anish' : 'python',
    'pasang' : 'java',
}
friends = ['pasang', 'anish']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favourite language is "
              + favourite_languages[name].title() + "!")
        
if 'jamuna' not in favourite_languages.keys():
    print("Jamuna, please take our poll.")

# Looping through a dictionary's key in order
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary
print("\nThe following languages has been mentioned: ")
for language in favourite_languages.values():
    print(language.title())