# using continue in a loop
# use continue statement to return to the beginning of the loop based on the result of a conditional test

current_number = 0
while current_number < 10:
    current_number += 1
    # if statement checks the modulo of current_number and 2
    # if modulo is 0, the continue statement tells python to ignore the rest of the loop
    # if current number is not divisible by 2, the rest of the loop is executed
    if current_number % 2 == 0:
        continue

    print(current_number)

# avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

# if you accidentally omit the x += 1, the loop will run forever
# this loop runs forever!
x = 1
while x <= 5:
    print(x)

# if your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window

# test every while loop and make sure the loop stops when you expect it to
# make sure at least one part of the program can make the loop's condition False
# or cause it to reach a break statement


