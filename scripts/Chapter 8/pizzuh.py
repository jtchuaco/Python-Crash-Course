# storing your functions in modules

# import statement tells python to make the code in a module available in the currently running porgram
# module is a file ending in .py that contains the code you want to import

# make a module that contains the function make_pizzuh()


def make_pizzuh(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

