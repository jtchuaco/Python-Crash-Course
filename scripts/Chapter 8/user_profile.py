# using arbitrary keyword arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    # add the first and last names to this dictionary because we'll always receive these two pieces of information
    profile['first_name'] = first
    profile['last_name'] = last
    # loop through the additional key-value pairs in dictionary user_info
    # and add each pair to the profile dictionary
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# remember to use the simplest approach that gets the job done
# as you progress, you'll learn to use the most efficient approach each time

