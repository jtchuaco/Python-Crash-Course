# return values
# the return statement takes a value from inside a function
# and sends it back to the line that called the function
# allows you to move much of your program's grunt work into functions

# returning a simple value
# defintion of get_formatted_name takes as parameters a first and last name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    # the function combines the two names and adds space between then
    # and store it in full_name
    full_name = first_name + ' ' + last_name
    # the value of full_name is converted to title case
    return full_name.title()
# when you call a function that returns a value
# you need to provide a variable where the return value can be stored
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making an argument optional
# you can use default values to make an argument optional

# first attempt to include middle names
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# however, middle names aren't always needed
# to make the middle name optional
# we can give the middle_name argument an empty default value
# and ignore the argument unless the user provides a value

# to make the function work without a middle name
# we set the default value of middle_name to an empty string
# and move it to the end of the list of parameters
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

