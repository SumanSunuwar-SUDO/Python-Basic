# A List of Dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'suman' : ['python, javascript'],
    'anish' : ['c'],
    'pasang' : ['java', 'c++'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())