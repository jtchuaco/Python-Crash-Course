# passing arguments
# positional arguments need to be in the same order the parameters were written

# definition shows that this function needs a type of animal and the animals name
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# the argument hamster is stored in the parameter animal_type
# the argument harry is stored in the parameter pet_name
describe_pet('hamster', 'harry')

# example of multiple function calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# order matters in positional arguments
# you can get unexpected results if you mix up the order of the arguments

# keyword arguments
# a name-value pair that you pass to a function
# free you from having to worry about correctly ordering your arguments in a function call

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# example of a keyword argument function call
describe_pet(animal_type='hamster', pet_name= 'harry')

# when you use keyword arguments,
# be sure to use the exact names of the parameters in the function's definition

# default values
# when writing a function, you can define a default value for each parameter

# included a default value, 'dog', for animal_type in the definition
# because the default value makes it unnecessary to specify a type of animal as an argument
# the only argument left in the function call in the pet's name
# that's why pet's name had to be the first parameter
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# when the function is called with no animal_type specified
# Python knows to use the value 'dog' for this parameter
describe_pet(pet_name='willie')

# avoiding argument errors
# unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work

# example when we call describe_pet() with no arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()

# breakdown of the error
# the traceback tells us the location of the problem
# the offending function call is written out for us to see
# traceback tells us the call is missing two arguments

