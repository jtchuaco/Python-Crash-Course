# modifying elements in a list
# original list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change first element of the list
motorcycles[0] = 'ducati'
print(motorcycles)

# appending elements to the end of a list
# the append() method adds the new element to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# append elements to an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements at any position in your list using insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list
# using the del statement
# when you use the del statement, the element is completely gone
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# removing elements
# using the pop() method
# the pop() method removes the last item in a list, but it lets you work with that item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# finding out the last motorcycle we bought using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# use pop() to remove an item in a list at any position by including the index of the item in the parentheses
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# removing elements
# using the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# can also use the remove() method to work with a value that's being removed from a list
# remove the value 'ducati' and print a reason for removing it
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + " is too expensive for me.")

