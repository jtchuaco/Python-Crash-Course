# use range() function to make a list of the first 10 square numbers
# the square of each integer from 1 through 10
# two asterisks (**) represent exponents
# start with an empty list
squares = []
# loop through each value from 1 to 10 using range() function
for value in range(1,11):
    # the current value is raised to the second power and stored in a new variable
    square = value**2
    # each new value of square is appended to the list squares
    squares.append(square)
# when the loop has finished running, the list of squares is printed
print(squares)

# to write the previous code concisely, you can omit the temporary variable square
# append each new value directly to the list
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# remember! focus first on writing code that you understand clearly, which does what you want it to do
# then look for more efficient approaches as you review your code

# simple statistics with a list of numbers
# min(), max(), sum() - specific to lists of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# minimum
min(digits)
# maximum
max(digits)
# sum
sum(digits)

# list comprehensions
# allows you to generate the same list in just one line of code
# combines the for loop and the creation of new elements into one line, and automatically appends each new element
# open a set of square brackets and define the expression for the values you want to store in the new list
# the expression here is value**2
# write a for loop to generate the numbers you want to feed into the expression, and close the square brackets
squares = [value**2 for value in range(1,11)]
print(squares)

