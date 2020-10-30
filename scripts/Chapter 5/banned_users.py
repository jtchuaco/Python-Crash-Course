# checking whether a value is in a list
# using the keyword 'in'

# make a list of toppings a customer has requested for a pizza
requested_toppings = ['mushrooms', 'onions', 'pineapple']
# check whether certain toppings are in the list
'mushrooms' in requested_toppings
# overall expression is True

'pepperoni' in requested_toppings
# overall expression is False

# checking whether a value is not in a list
# using the keyword 'not'

# make a list of users who are banned in a forum
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# check is user is in the list of banned_users
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# boolean expressions
# another name for conditional test
# boolean value is either True or False
# an efficient way to track the state of a program
# or a particular condition that is important in your program
