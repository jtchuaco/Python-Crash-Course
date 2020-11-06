# exercise 5-8. hello admin
# make a list of five or more user names, including the name admin
# imagine you are writing code that will print a greeting to each user after they log in to a website
# loop through the list
# print a greeting to each user
# if username is 'admin', print a special greeting
# otherwise, print a generic greeting

user_names = ['harry', 'hermione', 'admin', 'draco', 'ron', 'blaise']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello " + user_name.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ", thank you for logging in again.")

# exercise 5-9. No Users
# add an if test to exercise 5-8 to make sure the list of users is not empty
# if the list is empty, print the message We need to find some users!
# remove all the user names from your list, and make sure the correct message is printed

user_names = []
if user_names:
    for user_name in user_names:
        print("Hello " + user_name.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# exercise 5-10. Checking Use names
# make a list of five or more user names called current_users
current_users = ['harry', 'hermione', 'draco', 'ron', 'blaise']
# make another list of five user names called new_users
# make sure one or two of the new user names are also in the current_users list
new_users = ['luna', 'neville', 'draco', 'pansy', 'harry']
# loop through the new_users list to see if each new username has already been used
# if it has, print a message that the person will need to enter a new username
# if not, print a message saying that the username is available
for new_user in new_users:
    if new_user in current_users:
        print("Sorry, please enter a new username.")
    else:
        print("Username is available.")

# exercise 5-11. Ordinal Numbers
# store the numbers 1 through 9 in a list
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# loop through the list
# use an if-elif-else chain inside the loop to print the proper ordinal ending for each number
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + "st")
    elif ordinal_number == 2:
        print(str(ordinal_number) + "nd")
    elif ordinal_number == 3:
        print(str(ordinal_number) + "rd")
    else:
        print(str(ordinal_number) + "th")

