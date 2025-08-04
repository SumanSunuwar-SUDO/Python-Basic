favorite__places = {
    'aryan' : ['ilam', 'birgunj', 'darchula'],
    'kushal' : ['dhobi', 'tukucha', 'falame saghu'],
    'anuj' : ['bihar', 'chitwan', 'modi khola'],
}

for name, places in favorite__places.items():
    print("\nName: " + name.title())
    print("Favorite places: ")
    for place in places:
        print("\t", place.title())