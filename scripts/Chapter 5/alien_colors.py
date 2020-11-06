# exercise 5-3. alien colors # 1
# create a variable called alien_color
# assign it a value of 'green', 'yellow' or 'red'
# write an if statement to test whether the alien's color is green
# if yes, print a message that the player earned 5 points

alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points.")

# write another version that passes the if test and another that fails

alien_color = 'yellow'
if alien_color == 'yellow':
    print("You earned 10 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You earned another 5 points.")

# exercise 5-4. alien colors # 2
# choose a color for an alien and write an if-else chain
# if alien's color is green, print a statement that player just earned 5 points
# if not, print a statement that the player earned 10 points

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points.")
else:
    print("You earned 10 points.")

# write one version that runs the if block
alien_color = 'green'
if alien_color == 'green':
    print("You earned 10 points.")
else:
    print("Try again next time.")

# another version that runs the else block
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 15 points.")
else:
    print("Sorry, try again.")

# exercise 5-3. alien colors # 3
# turn your if-else chain from exercise 5-4 into an if-elif-else chain
# if alien is green, print a message that the player earned 5 points
# if alien is yellow, print a message that the player earned 10 points
# if alien is red, print a message that the player earned 15 points
# write three versions of this program, making sure each message is printed for the appropiate color alien.

alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# exercise 5-6. stages of life
# write an if-elif-else chain that determines a person's stage of life
# set a value for the variable age
# if person is less than 2, print a message that the person is a baby
# if at least 2 but less than 4, print a message that the person is a toddler
# if at least 4 but less than 13, print a message that the person is a kid
# if at least 13 but less than 20, print a message that the person is a teenager
# if at least 20 but less than 65, print a message that the person is an adult
# if 65 or older, print a message that the person is an elder

age = 33
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are an elder.")

# exercise 5-7. favorite fruit
# make a list of your favorite fruits
# write a series of independent if statements that check for certain fruits in your list

# make a list of your three favorite fruits
favorite_fruits = ['mango', 'banana', 'strawberry']

# write 5 if statements
# check if certain kind of fruit is in the list
# if the fruit is in the list, the if block should print a statement

if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'lemon' in favorite_fruits:
    print("You really like lemons!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")


