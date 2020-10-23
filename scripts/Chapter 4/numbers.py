# making numerical lists
# lists are ideal for storing sets of numbers

# using the range() function
# generate a series of numbers
for value in range(1,5):
    print(value)
# in the previous statement, it only prints the numbers 1 through 4
# this is because the range() function causes Python to start counting at the first value you give it,
# and it stops when it reaches the second value
# to print number from 1 to 5, use range(1,6)
for value in range(1,6):
    print(value)

# use range() to make a list of numbers
# convert the results of range() into a list by using the list() function
numbers = list(range(1,6))
print(numbers)


