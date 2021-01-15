# exercise 7-4. pizza toppings
# write a loop that prompts user to enter a series of pizza toppings
# until they enter a 'quit' value
# as they enter each topping, print a message saying you'll add that topping

prompt = "\nPlease enter the topping you want on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("I'll add " + topping + " to your pizza.")

# exercise 7-5. movie tickets
# a movie theater charges different ticket prices depending on age
# if a person is under the age of 3, the ticket is free
# if between 3 and 12, the ticket is $10
# if they are over 12, the ticket is $15
# write a loop in which you ask users their age
# then tell them the cost of their movie ticket

prompt = "\nPlease enter your age:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            print("Your ticket is free.")

        elif age >= 3 and age <= 12:
            print("Your ticket is $10.")

        else:
            print("Your ticket is $15.")

# exercise 7-6. three exits:
# write different versions of either exercise 7-4 or 7-5
# that do each of the following at least once
# use a conditional test in the while statement to stop the loop
# use an active variable to control how long the loop runs
# use a break statement to exist the loop when the user enters a 'quit' value

# using conditional test for exercise 7-4
prompt = "\nPlease enter the topping you want on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print("I'll add " + topping + " to your pizza.")
    else:
        print("Your pizza is ready.")

# using an active variable for exercise 7-5
prompt = "\nPlease enter your age:"
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("Your ticket is free.")

        elif age >= 3 and age <= 12:
            print("Your ticket is $10.")

        else:
            print("Your ticket is $15.")

# using break for exercise 7-4
prompt = "\nPlease enter the topping you want on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I'll add " + topping + " to your pizza.")

# exercise 7-7. infinity
# write a loop that never ends and run it

number = 7
while number <= 10:
    print(number)

