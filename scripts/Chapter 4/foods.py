# copying a list
# to copy a copy, make a slice that includes the entire original list by omitting the first index and the second index
my_foods= ['pizza', 'falafel', 'carrot cake']
# copy by using slice [:]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# add new food to each list to prove there are two separate lists
my_foods= ['pizza', 'falafel', 'carrot cake']
# copy by using slice [:]
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# when you try to copy a list without using a slice
my_foods = ['pizza', 'falafel', 'carrot cake']
# this doesn't work:
# as both variables point to the same list
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
