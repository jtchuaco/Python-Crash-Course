# exercise 4-10. slices
# using one of the programs you wrote in chapter 4, add several lines to the end of the program
pizzas = ['pepperoni', 'all meat', 'four cheese', 'margharita', 'truffle']

# print the message, The first three items in the lists are:
# then use a slice to print the first three items
print("The first three items in the list are:")
print(pizzas[0:3])

# print the message, Three items from the middle of the list are:
# use a slice to print three items from the middle of the list
pizzas = ['pepperoni', 'all meat', 'four cheese', 'margharita', 'truffle']

print("Three items from the middle of the list are:")
print(pizzas[1:4])

# print the message: The last three items in the list are:
# use a slice to print the last three items in the list
pizzas = ['pepperoni', 'all meat', 'four cheese', 'margharita', 'truffle']

print("The last three items in the list are:")
print(pizzas[2:])

# exercise 4-11. my pizzas, your pizzas
# start with your program from exercise 4-1
# make a copy of the list of pizzas, call it friend_pizzas

my_pizzas = ['pepperoni', 'all meat', 'four cheese']
friend_pizzas = my_pizzas[:]
# add a new pizza to the original list
my_pizzas.append('margharita')
# add a different pizza to the list friend_pizzas
friend_pizzas.append('bacon')
# prove that you have two separate lists
# print the message, My favorite pizzas are:, and then use a for loop to print the first list
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
# print the message, My friend's favorite pizzas are:, and then use a for loop to print the second list
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# exercise 4-12. more loops
# choose a version of foods.py
# write two for loops to print each list of foods
my_foods= ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

