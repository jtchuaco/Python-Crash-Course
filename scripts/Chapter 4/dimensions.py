# tuples - immutable list or a list that cannot change
# define tuples by using a parentheses instead of square brackets
dimensions = (200, 50)
# print each element in tuple by using same syntax we use in accessing elements in a list
print(dimensions[0])
print(dimensions[1])
# try to change one of the items in the tuple
# will return an error because we can't assign a new value to an item in a tuple
dimensions[0] = 250

# looping through a tuple
# same principle as with a list
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# writing over a tuple
# can't modify a tuple, but can assign a new value to a variable that holds a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# store a new tuple in the variable dimensions
dimensions = (400, 100)
# did not raise any errors, because overwriting a variable is valid
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# tuples are simple data structures
# use them when you want to store a set of values that should not be changed throughout the life of a program
