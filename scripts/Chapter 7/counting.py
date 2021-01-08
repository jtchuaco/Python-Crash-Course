# while loop
# runs as long as a certain condition is true
# use to count through a series of numbers

# start by setting the value to 1
current_number = 1
# set to keep running as long as the value is less than or equal to 5
while current_number <= 5:
    # prints the value of the current number
    print(current_number)
    # adds 1 to that value
    # += operator is shorthand for current_number = current_number + 1
    current_number += 1

# letting the user choose when to quit

# tells user their two options
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# store whatever value the user enters
message = ""
# while loop runs as long as the value of message is not quit
while message != 'quit':
    message = input(prompt)
    print(message)
    # it works well, except it prints the word quit as if it were an actual message
    # a simple if test fixes this:
    if message != 'quit':
        print(message)

# using a flag
# flag acts as a signal to the program
# the program will run while the flag is set to True
# and stop when any of several events sets the value of the flag to False

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# program starts in an active state
active = True
# as long as the active variable remains True, the loop will continue running
while active:
    message = input (prompt)
    # if the user enters 'quit', we set active to False and while loop stops
    if message == 'quit':
        active = False
    # if user enters anything other than 'quit', print their input as a message
    else:
        print(message)

