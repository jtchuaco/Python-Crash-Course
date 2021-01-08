# using int() to accept numerical input
# when you use the input() function: Python interprets it as a string

age = input("How old are you? ")
print(age)

# when user enters the number, Python returns the value enclosed in quotes
# if all you want is print the input, this works
# if you try to use the input as a number, you'll get an error

age = input("How old are you? ")
# produces an error because it can't compare a string to an integer
age >= 18

# use int() function which tells Python to treat the input as a numerical value
# convert a string representation of a number to a numerical representation

age = input("How old are you? ")
# the value is converted to a numerical representation by int()
age = int(age)
# Python can now run the conditional test
age >= 18
# this test evaluates to a True

# how to use the int() function in an actual program
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# when you use numerical input to do calculations and comparisons,
# be sure to convert the input value to a numerical representation first

