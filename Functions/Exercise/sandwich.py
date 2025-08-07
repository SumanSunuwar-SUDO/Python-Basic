def make_sandwiches(*items):
    print("\nSandwiches that is being ordered: ")
    for item in items:
        print("- " + item)

make_sandwiches('Ham','cheese')
make_sandwiches("Club Sandwich", "Grilled Cheese",)