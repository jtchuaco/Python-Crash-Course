# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    # the value of first_name is stored with the key 'first'
    # and the value of last_name is stored with the key 'last'
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# change the earlier script to allow you to store a person's age
# add a new optional parameter age to the function definition
# and assign the parameter an empty default value
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

