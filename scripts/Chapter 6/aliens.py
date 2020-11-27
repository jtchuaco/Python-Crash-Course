# nesting
# storing a set of dictionaries in a list
# or a list of items as a value in a dictionary

# a list of dictionaries
# create three dictionaries each representing a different alien
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# pack the dictionaries into a list called aliens
aliens = [alien_0, alien_1, alien_2]
# loop through the list to print out each alien
for alien in aliens:
    print(alien)

# use range()
# range() returns a set of numbers, which tells Python how many times we want to loop to repeat
# make an empty list for storing aliens
aliens = []

# make 30 green aliens
# use range() to tell Python how many times the loop should repeat
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# append each new alien to the list aliens
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))

# change the first three aliens to yellow, medium-speed worth 10 points
# modify it using the if statement
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# expand the loop by adding an elif block
# change yellow aliens to red, fast-moving ones worth 15 points
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# remember: all of the dictionaries in the list should have an identitical structure
