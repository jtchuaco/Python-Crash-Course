# exercise 8-15. printing models
# put the functions for the example printing_models.py
# in a separate file called printing_functions.py
# write an import statement at the top of print_models.py
# modify the file to use the imported functions

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# exercise 8-16. imports
# using a program you wrote that has one function in it
# store that function in a separate file
# import the function into your main program file
# call the function using each of these approaches
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# import module_name
import pet_functions

pet_functions.describe_pet('dog', 'hachi')

# from module_name import function_name
from pet_functions import describe_pet

describe_pet('dog', 'hachi')

# from module_name import function_name as fn
from pet_functions import describe_pet as dp

dp('dog', 'hachi')

# import module_name as mn
import pet_functions as pf

pf.describe_pet('dog', 'hachi')

# from module_name import *
from pet_functions import *

describe_pet('dog', 'hachi')

