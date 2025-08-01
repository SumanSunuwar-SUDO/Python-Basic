# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Conditional Tests
    # Check for equality
car = 'bmw'
print(car == 'bmw') 
print(car == 'audi')  

    # Ignoring case when checking for equality
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')