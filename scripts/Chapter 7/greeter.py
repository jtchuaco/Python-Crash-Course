# writing clear prompts
# should include a clear, easy-to-follow prompt

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# add a space at the end of your prompts
# to make it clear to your user where to enter their text

# example to build a multi-line string
# stores the first part of the message
prompt = "If you tell us who you are, we can personalize the messages you see."
# the operator += takes the string that was stored in prompt and
# adds the new string onto the end
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

