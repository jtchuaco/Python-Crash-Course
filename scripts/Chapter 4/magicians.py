# looping through an entire list
# print out each name in a list of magicians
# begin by defining a list
magicians = ['alice', 'david', 'carolina']
# use a for loop
# in the for loop, we tell Python to print the name that was stored in the list
# "For every magician in the list of magicians, print the magician's name."
for magician in magicians:
    print(magician)

# remember! helpful to choose a meaningful name that represents a single item in the list

# doing more work within a loop
# remember! every indented line following the line 'for magician in magicians' is considered inside the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# the newline ("\n") inserts a blank line after each pass through the loop

# doing something after a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# any lines after the for loop that are not indented are executed once without repetition
print("Thank you, everyone. That was a great magic show!")

# common indentation errors
# forgetting to indent
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
# error: the print statement should be indented

# forgetting to indent additional lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
# the syntax is valid python code, but it didn't do what the expected result is
# therefore, this is a logical error

# indenting unnecessarily
message = "Hello Python world!"
    print(message)
# error: unexpected indent in print statement
# remember! the only lines you should indent are the actions you want to repeat for each item in a for loop

# indenting unnecessarily after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")
# this is also a logical error, because what you wanted was the last line to only print once
# if an action is repeated many times when it should be executed only once,
# determine whether you just need to unindent the code for that action

# forgetting the colon
# the colon at the end of a for statement tells python to interpret the next line as the start of a loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)
# error: invalid syntax, because Python doesn't know what you're trying to do