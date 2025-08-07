def make_car(manufacture, model, **car_info):
    '''Summarizing detail about a car'''
    cars = {}
    cars['manufacture_name'] = manufacture
    cars['model_name'] = model
    for key, value in car_info.items():
        cars[key] = value
    
    return cars

car_detail = make_car("Subaru", "Outback", color = 'blue', tow_package=True)
print(car_detail)