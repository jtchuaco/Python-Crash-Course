# this file imports the module we just created in pizzuh.py

# the line import tells Python to open the file puzzuh.py
# it copies all the functions into this program
import pizzuh

# to call a function from an imported module
# enter the name of the module you imported followed by the name of the function
# separate them by a dot
# syntax module_name.function_name()
pizzuh.make_pizzuh(16, 'pepperoni')
pizzuh.make_pizzuh(12, 'mushrooms', 'green peppers', 'extra cheese')


# importing specific functions
# syntax for this approach: from module_name import function_name
# you can import as many functions, separate each function name with a comma

from pizzuh import make_pizzuh

make_pizzuh(16, 'pepperoni')
make_pizzuh(12, 'mushrooms', 'green peppers', 'extra cheese')


# using as to give a function an alias
# alias is an alternate name similar to a nickname for the function
# syntax for this: from module_name import function_name as fn

from pizzuh import make_pizzuh as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# using as to give a module an alias
# symtax for this approach: import module_name as mn

import pizzuh as p

p.make_pizzuh(16, 'pepperoni')
p.make_pizzuh(12, 'mushrooms', 'green peppers', 'extra cheese')


# importing all functions in a module
# syntax: from module_name import *

from pizzuh import *

make_pizzuh(16, 'pepperoni')
make_pizzuh(12, 'mushrooms', 'green peppers', 'extra cheese')

# styling functions
# functions should have descriptive names
# should use lowercase letters and underscores
# every function should have a comment that explains concisely what the function does
# if you specify a default value for a parameter, no space should be used on either side of the equal sign
# example: def function_name(parameter_0, parameter_1='default value')

# all import statements should be written at the beginning of a file
