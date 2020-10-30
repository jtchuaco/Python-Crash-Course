# write code that's easier to read
# read the PEP 8 guidelines
# some guidelines in writing a clear code:
# a. indentation - four spaces per indentation
# b. line length - less than 80 characters
# c. comments should be just 72 characters per line
# d. blank lines - use to organize your files

# exercise 4-14. PEP 8
# look through PEP 8 style guide
# https://python.org/dev/peps/pep-0008/

# exercise 4-15. code review
# choose three of the programs you've written and modify each one to comply with PEP 8
# use four spaces for each indentation level
# use less than 80 characters on each line
# don't use blank lines excessively

# original code no. 1
buffet = ('beef', 'chicken', 'fish', 'pork', 'rice')
# use a for loop to print each food the restaurant offers
print("This restaurant only offers the following:")
for food in buffet:
    print(food)

# modified to PEP 8
buffet = (
    'beef', 'chicken', 'fish',
    'pork', 'rice'
 )

print('This restaurant only offers the following:')
for food in buffet:
    print(food)

# original code no. 2
pizzas = ['pepperoni', 'all meat', 'four cheese', 'margharita', 'truffle']

print("Three items from the middle of the list are:")
print(pizzas[1:4])

# modified to PEP 8
pizzas = [
    'pepperoni', 'all meat',
    'four cheese', 'margharita',
    'truffle'
]

print("Three items from the middle of the list are:")
print(pizzas[1:4])

# original code no. 3
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# modified to PEP 8
digits = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    0
]

