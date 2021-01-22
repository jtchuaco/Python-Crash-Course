# exercise 7-8. deli
# make a list called sandwich_orders
# fill it with the names of various sandwiches
# make an empty list called finished_sandwiches
# loop through the list of orders and print a message for each order
# as each sandwich is made, move it to the list of finished sandwiches
# after all the sandwiches have been made,
# print a message listing each sandwich that was made

# list of sandwiches
sandwich_orders = ['tuna', 'chicken', 'turkey', 'ham', 'egg mayo']

# empty list
finished_sandwiches = []

# loop through the orders
while sandwich_orders:
    made_sandwiches = sandwich_orders.pop()

    # print a message for each order
    print("I have made you a " + made_sandwiches + " sandwich.")
    # move it to list of finished_sandwiches
    finished_sandwiches.append(made_sandwiches)

# Print a message listing each sandwich that was made
print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# exercise 7-9. no pastrami
# using sandwich_orders list from 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three times
# add code near the beginning to print a message saying,
# the deli has run out of pastrami
# use a while loop to remove all occurrences of 'pastrami'
# make sure no pastrami sandwiches end up in finished_sandwiches

# list of sandwiches
sandwich_orders = ['pastrami', 'tuna', 'chicken',
                   'ham', 'pastrami', 'turkey',
                   'egg mayo', 'pastrami', 'pastrami']

# empty list
finished_sandwiches = []

# print a message saying the deli has run out of pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nSorry, the deli ran out of pastrami.")

# make sure no pastrami sandwiches end up in finished_sandwiches
while sandwich_orders:
    final_orders = sandwich_orders.pop()
    finished_sandwiches.append(final_orders)

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# exercise 7-10. dream vacation
# write a program that polls users about their vacation
# write a prompt 'If you could visit one place in the world, where would you go?'
# include a block of code that prints the results of the poll

# poll users about their dream vacation
answers = {}

polling_active = True

while polling_active:
    name = input("\nHi, what is your name?")
    answer = input("If you could visit one place in the world,"
                   " where would you go? ")

    answers[name] = answer

    repeat = input("Would you like to ask another person? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# print the results of the poll
print("\n--- Poll Results ---")
for name, answer in answers.items():
    print(name.title() + " would like to go to " + answer.title() + ".")

