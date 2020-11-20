# exercise 6-4. glossary 2
# clean up the code from exercise 6-3
glossary = {
    'strip': 'use to remove the whitespace from a string',
    'variable': 'use to hold a value',
    'string': 'a series of characters',
    'method': 'an action that Python can perform on a piece of data',
    'float': 'any number with a decimal point'
}

print('strip: ' + glossary['strip'],
      '\nvariable: ' + glossary['variable'],
      '\nstring: ' + glossary['string'],
      '\nmethod: ' + glossary['method'],
      '\nfloat: ' + glossary['float'])

# replace the series of print statements with a loop
for key, value in glossary.items():
    print(key + ': ' + value)

# when the loop works, add five more Python terms to your glossary
glossary['list'] = 'a collection of items in a particular order'
glossary['append'] = 'simplest way to add a new element to a list'
glossary['insert'] = 'add a new element at any position in your list'
glossary['del'] = 'remove an item or a set of items from a list'
glossary['pop'] = 'removes the last item in a list'

# run your loop again, the new words and meanings should automatically be included
for key, value in glossary.items():
    print(key + ': ' + value)


# exercise 6-5. rivers
# make a dictionary containing three major rivers and the country each river runs through
rivers = {
    'nile river': 'egypt',
    'yangtze river': 'china',
    'amazon river': 'south america',
}

# use a loop to print a sentence about each river
for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title() + '.')

# use a loop to print the name of each river
for river in rivers.keys():
    print(river.title())

# use a loop to print the name of each country
for country in rivers.values():
    print(country.title())

# exercise 6-6. polling
favorite_languages = {
    'nicole': 'python',
    'kaye': 'r',
    'sarah': 'c',
    'mark': 'python',
    'hj': 'python',
    'jon': 'python',
    'edward': 'ruby',
}
# make a list of people who should take the favorite languages poll
to_poll = ['brent', 'nicole', 'mark', 'neil', 'jon', 'hj', 'kaye', 'ino']

# loop through the list of people who should take the poll
# if they have taken the poll, print a message thanking them
# if not, print a message inviting them to take a poll

for name in to_poll:
    if name in favorite_languages:
        print(name.title() + ', thank you for taking our poll.')
    if name not in favorite_languages:
        print(name.title() + ', please take our poll. Thank you.')

