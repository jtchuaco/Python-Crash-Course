# exercise 8-12. sandwiches
# write a function that accepts a list of items a person wants on a sandwich
# should have one parameter that collects as many items as the function call provides
# print a summary of the sandwich that is being ordered
# call the function three times
# using a different number of arguments each time

def make_sandwich(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking you a great sandwich:")
    for item in items:
        print("Adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('tuna', 'tomato', 'onion', 'lettuce')
make_sandwich('ham', 'cheese')
make_sandwich('roast chicken', 'lettuce', 'jalapeno', 'honey mustard', 'sweet onion')

# exercise 8-13. user profile
# start with a copy of user_profile.py from page 153
# build a profile of yourself by calling build_profile()
# use your first and last names and three other key-value pairs that describes you

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

user_profile = build_profile('judy', 'chua',
                             color='blue',
                             likes='eating',
                             hobby='sleeping')

print(user_profile)

# exercise 8-14. cars
# write a function that stores information about a car in a dictionary
# function should always receive a manufacturer and a model name
# should accept an arbitrary number of keyword arguments
# call the function with the required information and two other name-value pairs

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about the car."""
    car_profile = {}
    car_profile['manufacturer_name'] = manufacturer
    car_profile['model_name'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car = make_car('subaru', 'outback', color='blue', tow_package='True')

my_car = make_car('toyota', 'vios', color='white', year='2016')

print(car)
print(my_car)


