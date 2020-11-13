# exercise 6-1. person
# use a dictionary to store information about a person
# store their first name, last name, age, and city
# print each information stored in your dictionary

person = {
    'first_name': 'Sean',
    'last_name': 'Tiu',
    'age': 24,
    'city': 'Manila'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# exercise 6-2. favorite numbers
# use a dictionary to store people's favorite number
# think of five names, use them as keys
# print each person's name and their favorite number
# poll a few friends and get some actual data
favorite_numbers = {
    'kaye': 7,
    'nicole': 3,
    'neil': 16,
    'sean': 17,
    'jd': 7
}

print("Kaye's favorite number is " +
      str(favorite_numbers['kaye']) +
      ".")
print("Nicole's favorite number is " +
      str(favorite_numbers['nicole']) +
      ".")
print("Neil's favorite number is " +
      str(favorite_numbers['neil']) +
      ".")
print("Sean's favorite number is " +
      str(favorite_numbers['sean']) +
      ".")
print("JD's favorite number is " +
      str(favorite_numbers['jd']) +
      ".")

# exercise 6-3. glossary
# think of five programming words you've learned
# use these words as the keys in your glossary
# store their meanings as values
# print each word and its meaning as neatly formatted output
# use the newline character to insert a blank line between each word-meaning pair

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






