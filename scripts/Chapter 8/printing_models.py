# modifying a list in a function
# any changes made to the list inside the function's body are permanent

# start with some deigns that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design, until none are left.
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# reorganize the above code by writing two functions
# each of which does one specific job
# first function will handle printing the designs
# the second will summarize the prints that have been made

# define the function with two parameters
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# define the second function with one parameter: list of completed models
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# if you're writing a function
# and notice the function doing too many different tasks
# split the code into two functions
# you can always call a function from another function

# preventing a function from modifying a list
# use function_name(list_name[:]) to make a copy of the list, not the original
# the slice notation [:] makes a copy of the list




