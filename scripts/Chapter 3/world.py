# exercise 3-8. seeing the world
# list at least five places in the world you'd like to visit
# not alphabetical
destination = ['japan', 'france', 'london', 'prague', 'iceland']
# print
print(destination)
# use sorted()
print(sorted(destination))
# print original list
print(destination)
# use reverse() to change the order
# print the list to show it's back to its original order
destination.reverse()
print(destination)
# use sort() to change your list
# print to show that its order has been changed
destination.sort()
print(destination)
# use sort() to change your list so it's stored in reverse alphabetical
# print the new list
destination.sort(reverse=True)
print(destination)

# exercise 3-9. dinner guests
# use len() to print a message indicating the number of people you are inviting to dinner
guests = ['Mark', 'Nicole', 'Kaye', 'Ino']
print("The number of guests I'm inviting is:")
print(len(guests))

# exercise 3-10. every function
# create a list of anything you like and write a program that uses each function in chapter 3 at least once
foods = ['siomai', 'pizza', 'milktea', 'cake', 'takoyaki']
print(foods)
# insert sisig at the middle
foods.insert(3, 'sisig')
print(foods)
# append icecream
foods.append('icecream')
print(foods)
# sorted() function
print(sorted(foods))
print(foods)
# remove sisig
foods.remove('sisig')
print(foods)
# reverse() function
foods.reverse()
print(foods)
# sort() function
foods.sort()
print(foods)
# pop the last element
popped_foods = foods.pop()
print(foods)
# reverse using sort() function
foods.sort(reverse=True)
print(foods)
# delete pizza
del foods[1]
print(foods)
# len() function
print("How many food is left in the list?")
print(len(foods))

