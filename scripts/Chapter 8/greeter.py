# defining a function
# functions are named blocks of code that are designed to do one specific job

# use the keyword def to inform Python you're defining a function
# function definition tells Python the name of the function and,
# if applicable, what kind of information the function needs to do its job
def greet_user():
    # docstring describes what the function does
    # enclosed in triple quotes
    """Display a simple greeting."""
    # the only line of actual code in the body of this function
    print("Hello!")
# function call tells Python to execute the code
# to call a function, you write the name of the function
# followed by any necessary information in parenthesis
greet_user()

# passing information to a function
# you can enter information in the parentheses of the function's definition

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

# arguments and parameters
# parameter is a piece of information the function needs to do its job
# argument is a piece of information that is passed from a function call to a function

