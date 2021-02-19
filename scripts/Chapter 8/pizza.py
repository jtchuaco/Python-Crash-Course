# passing an arbitrary number of arguments
# example, consider a function that builds a pizza
# needs to accept a number of toppings
# but you can't know ahead of time how many toppings a person will want

# the asterisk in the parameter name tells Python to make an empty tuple
# and pack whatever value it receives into this tuple
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# replace the print statement with a loop that runs through the list of toppings
# describe the pizza being ordered

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mixing positional and arbitrary arguments
# if you want a function to accept several different kinds of arguments
# the parameter that accepts an arbitrary number of arguments must be placed last in the function definition

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')