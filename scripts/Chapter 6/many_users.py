# a dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einsten',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
# loop through the users dictionary
# python stores each key in the variable username
# the dictionary associated with each username goes into the variable user_info
for username, user_info in users.items():
    # once inside the main dictionary loop, print the username
    print("\nUsername: " + username)
    # start accessing the inner dictionary
    # the dictionary of user information has three keys: first, last, and location
    # use each key to generate a neatly formatted full name and location for each person
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
# then print a summary of what we know about each user
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

