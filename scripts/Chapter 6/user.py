# looping through a dictionary
# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# if you wanted to see everything stored
# use a for loop
# create names for the two variables that will hold the key and value in each key-value pair
# include the name of the dictionary followed by the method items
# the items() method returns a list of key-value pairs
for key, value in user_0.items():
    # use the variables to print each key, followed by the associated value
    print("\nKey: " + key)
    print("Value: " + value)

# another example
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# looping through all the keys in a dictionary
# use the keys() method
# pull all the keys from the dictionary and store them one at a time in the variable name
for name in favorite_languages.keys():
    print(name.title())

# looping through keys is actually the default behavior when looping through a dictionary
# make a list of friends we want to print a message to
friends = ['phil', 'sarah']
# inside the loop, print each person's name
for name in favorite_languages.keys():
    print(name.title())
    # check to see whether the name is in the list of friends
    if name in friends:
        # if yes, print a special message
        # use the name of the dictionary and the current value of name as the key
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# find out if Erin took the poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# the if statement simply checks if erin is in the list
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionary's keys in order
# use sorted() function to get a copy of the keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# looping through all values in a dictionary
# use values() method to return a list of values without any keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# to see each values chosen without repetition, use a set
# set is similar to a list except that each item in the set must be unique
# use set() to pull out the unique languages
for language in set(favorite_languages.values()):
    print(language.title())

