# exercise 8-9. magicians
# make a list of magician's names
# pass the list to a function called show_magicians()
# print the name of each magician in the list


def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())


magicians = ['harry houdini', 'david blaine', 'harry potter']
show_magicians(magicians)

# exercise 8-10. great magicians
# start with your program from exercise 8-9
# write a function called make_great() that modifies the list of magicians
# by adding the phrase the Great to each magician's name
# call show_magicians() to see that the list has actually been modified


def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Add the Great at the end of each magician name in the list."""
    great_magicians = []

    while magicians:
        add_great_magician = magicians.pop()
        great_magician = add_great_magician + ' the Great'
        great_magicians.append(great_magician)

    for greatness in great_magicians:
        magicians.append(greatness)


magicians = ['harry houdini', 'david blaine', 'harry potter']

print("\n")
make_great(magicians)
show_magicians(magicians)

# exercise 8-11. unchanged magicians
# start with your program from exercise 8-10
# call function make_great() with a copy of the list of magicians' names
# because the original list will be unchanged, return the new list and store it in separate list
# call show_magicians with each list to show that you have one list of the original names
# and one list with the great added to each magician's name

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Add the Great at the end of each magician name in the list."""
    while magicians:
        add_great_magician = magicians.pop()
        great_magician = add_great_magician + ' the Great'
        great_magicians.append(great_magician)

    for greatness in great_magicians:
        magicians.append(greatness)

    return magicians

magicians = ['harry houdini', 'david blaine', 'harry potter']
great_magicians = []

# magicians with the Great at the end
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

# original magicians
show_magicians(magicians)

