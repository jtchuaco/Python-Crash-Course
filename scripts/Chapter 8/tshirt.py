# exercise 8-3. T-shirt
# write a function called make_shirt()
# that accepts a size and the text of a message that should be printed on the shirt
# should print a sentence summarizing the size and the message
# use positional arguments for the first time
# user keyword arguments for the second time

def make_shirt(size, message):
    """Display the size and the message you want on your shirt."""
    print("\nI'm going to make a " + size + "-sized shirt.")
    print("It will have a phrase that says: " + message.title() + ".")

make_shirt('medium', 'make it count')
make_shirt(size='large', message='trust the process')

# exercise 8-4. large shirt
# modify the make_shirt() function
# that shirts are large by default with a message that reads I love Python
# make a large shirt and a medium shirt with the default message
# and a shirt of any size with a different message

def make_shirt(size='large', message='i love python'):
    """Display the size and the message you want on your shirt."""
    print("\nI'm going to make a " + size + "-sized shirt.")
    print("It will have a phrase that says: " + message.title() + ".")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='i like sql more')

# exercise 8-5. cities
# write a function called describe_city()
# that accepts the name of a city and its country
# should print a simple sentence
# give the parameter for the country a default value
# call your function for three different cities
# at least one of which is not in the default country

def describe_city(city, country='South Korea'):
    """Describe a city."""
    print(city.title() + ' is in ' + country.title() + ".")

describe_city('incheon')
describe_city('seoul')
describe_city('tokyo', 'japan')

