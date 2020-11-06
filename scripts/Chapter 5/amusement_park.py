# if-elif-else chain
# use this is you need to test more than two possible situations

# how to determine a person's admission rate
age = 12
# test whether a person is under 4 years old
if age < 4:
    print("Your admission cost is $0.")
# elif line runs only if the previous test failed
elif age < 18:
    print("Your admission cost is $5.")
# if both the if and elif tests fail, python runs the else
else:
    print("Your admission cost is $10.")

# rather than printing the admission price
# more concise to set the price inside the if-elif-else chain

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# using multiple elif blocks
# add one more conditional test to the code above
# determine whether someone qualified for the senior discount

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
# the value was changed because the only ages that make it to this block are people 65 or older
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# omitting the else block
# python does not require an else block at the end of an if-elif chain
# clearer to use an additional elif statement that catches specific condition of interest

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
# this is clearer than the general else block
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# remember, the else block is a catchall statement

# testing multiple conditions
# using a series of simple if statements

# list containing the requested toppings
requested_toppings = ['mushrooms', 'extra cheese']
# checks to see if the topping is in the list
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
# another if statement, this test runs regardless of the whether the previous test passed or not
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
# checks whether extra cheese was requested regardless of results from the first two tests
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# if you want only one block of code to run, use an if-elif-else chain
# if more than one block of code needs to run, use a series of independent if statements

