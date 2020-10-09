# exercise 2-3. Personal message
# store a person's name in a variable, and print a message to that person
f_name = "judy"
print("Hello " + f_name.title() + ", " + "would you like to learn some Python today?")

# exercise 2-4. Name Cases
# store a person's name in a variable, and then print that person's name in lowercase, uppercase, and titlecase
name_1 = "danni"
print(name_1.lower())
print(name_1.upper())
print(name_1.title())

# exercise 2-5. Famous Quote
# find a quote from a famous person. Print the quote and the name of its author. should include quotation marks.
print('Theodore Roosevelt once said, "It is hard to fail\nbut it is worse never to have tried to succeed."')

# exercise 2-6. famous quote 2
# repeat 2-5, but store the famous person's name in a variable called famous_person.
# compose your message and store it in a new variable called message
famous_person = "Theodore Roosevelt"
message = famous_person.title() + 'once said, "It is hard to fail\nbut it is worse never to have tried to succeed."'
print(message)

# exercise 2-7. stripping names
# store a person's name, and include some whitespace characters at the beginning and end of the name
# use each character combination, "\t" and "\n", at least once
# print the name once to have the whitespace displayed and then print the name using each of the three strip functions
name_2 = " judy "
print(name_2)

name_2 = name_2.rstrip()
print(name_2)

name_2 = name_2.lstrip()
print(name_2)

name_2 = name_2.strip()
print(name_2)

