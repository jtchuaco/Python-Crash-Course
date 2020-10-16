# Create a list of kinds of bicycles
# square brackets [ ] indicate a list in python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# access any element in a list by using index
# index positions start at 0, not 1
print(bicycles[0])

# format the element by using the title() method
print(bicycles[0].title())

# access the 2nd and 4th item in bicycles
print(bicycles[1])
print(bicycles[3])

# special syntax [-1] for accessing the last element in the list
print(bicycles[-1])

# use concatenation to create a message based on a value from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)