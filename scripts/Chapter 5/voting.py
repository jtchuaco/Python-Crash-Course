# simple if statements
# if True, Python executes the code following the if statement
# if False, Python ignores the code following the if statement
# can have as many lines of code following the if statement

# testing if a person is old enough to vote
age = 19
# checks whether the value in age is greater than or equal to 18
if age > 18:
    # if yes, python executes the indented print statement
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else statements
# else statement allows you to define an action when the conditional test fails
# works well in situations where there is just one of two possible actions

age = 17
# if True, the first block of indented print statements is executed
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# if False, the else statement is executed
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

