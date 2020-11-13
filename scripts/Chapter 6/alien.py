# simple dictionary
# example of a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# dictionary in Python is a collection of key-value pairs
# each key is connected to a value
# use a key to access the value associated with that key
# key's value can be a number, a string, a list, or even another dictionary
# a dictionary is wrapped in braces {}
alien_0 = {'color': 'green', 'points': 5}
# every key is connected to its value by a colon
# individual key-value pairs are separated by commas

# example of a one key-value pair
alien_0 = {'color': 'green'}
# color is a key in this dictionary
# green is the associated value
print(alien_0['color'])


alien_0 = {'color': 'green', 'points': 5}
# pulls the value associated with the key 'points'
new_points = alien_0['points']
# converts this integer value to a string
print("You just earned " + str(new_points) + " points!")

# adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# add a new key-value pair: key 'x_position' value 0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# print the modified dictionary
print(alien_0)

# empty dictionary
# use when storing user-supplied data
# or when you write code that generates a large number of key-value pairs
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary
# put the key in a square bracket and the new value associated with the key
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
# change the alien's color to yellow
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# removing key-value pairs
# use the del statement to completely remove a key-value pair
# provide name of the dictionary and the key you want to remove
# once you use del, the key-value pair is removed permanently

# original dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# remove points from the alien_0 dictionary
del alien_0['points']
print(alien_0)
