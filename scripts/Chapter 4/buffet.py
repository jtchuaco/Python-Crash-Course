# exercise 4-13. buffet
# think of five simple foods, store them in a tuple
buffet = ('beef', 'chicken', 'fish', 'pork', 'rice')
# use a for loop to print each food the restaurant offers
print("This restaurant only offers the following:")
for food in buffet:
    print(food)
# try to modify one of the items, and make sure Python rejects the change
buffet[0] = 'lamb'
# replace two items in the menu
# add a block of code that rewrites the tuple
buffet = ('roast beef', 'chicken', 'lobster', 'pork', 'rice')
# use a for loop to print each of the items on the revised menu
print("\nThis restaurant now offers the following:")
for food in buffet:
    print(food)

