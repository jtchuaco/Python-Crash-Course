# Using break to Exit a Loop
# use break statement to exit a while loop immediately without running any remaining code in the loop
# it directs the flow of your program
# use it to control which lines of codes are executed and which aren't

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# will run forever unless it reaches a break statement
# when user enter quit, the break statement runs, causing Python to exit the loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go " + city.title() + "!")

# can use the break statement in any of Python's loop




