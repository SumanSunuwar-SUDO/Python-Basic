import pizza
# importing entire module
# module_name.function_name()

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# importing specific functions
# from module_name import function_name
# from module_name import function1. function2, function3;

from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function an Alias
# from module_name import function_name as fn
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# Using as to Give a Module an Alias
import pizza as p
p.make_pizza(12, 'mushrooms', 'green peppers')

# importing all functions in a module
# from module_name import *

from pizza import *
make_pizza(14, "extra cheese")

# Styling Functions
"""def function_name(parameter_0, parameter_1="default value"):
    function body ...
"""