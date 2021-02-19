# passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

# define a list of users and then pass the list usernames to greet_users in our function call
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)