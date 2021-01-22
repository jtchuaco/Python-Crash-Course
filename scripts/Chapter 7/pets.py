# removing all instances of specific values from a list
# remove() : to remove a specific value from a list
# if you want to remove all instances of that value,
# run a while loop

# start with a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# after printing the list, Python enters the while loop
print(pets)
# once inside loop, Python removes the first instance of 'cat',
# returns to the while line,
# and then reenters the loop when it finds that 'cat' is still in the list
while 'cat' in pets:
    pets.remove('cat')
# when the value is no longer in the list
# Python exists the loop and prints the list again
print(pets)



