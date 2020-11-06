# using if statements with lists
# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# what if the pizzeria runs out of green peppers?
# an if statement inside the for loop can handle this situation appropriately

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    # check to see if the person requested green peppers
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    # ensures that all other toppings will be added to the pizza
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# checking that a list is not empty
requested_toppings = []
# if a name of a list is used in an if statement
# python returns True if the list contains at least one item
# an empty list evaluates to a false
# if requested_toppings passes the conditional test, we run the for loop
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
# if it fails, we print a message asking customer if they want a plain pizza
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
# define a list of available toppings
available_toppings = ['mushrooms', ' olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
# make a list of toppings that a customer has requested
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# loop through the list of requested_toppings
for requested_topping in requested_toppings:
    # inside the loop, check if each requested topping is actually in the list of available topping
    if requested_topping in available_toppings:
        # if True, add that topping to the pizza
        print("Adding " + requested_topping + ".")
    # if False, print a message that tells users which toppings are unavailable
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

