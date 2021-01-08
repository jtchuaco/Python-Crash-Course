# exercise 7-1. rental car
# write a program that asks the user what kind of rental car they would like
# print a message about that car

rental_car = input("What kind of rental car do you like? ")
print("Let me see if I can find you a " + rental_car + ".")

# exercise 7-2. restaurant seating
# write a program that asks the user how many people are in their dinner group
# if the answer is more than eight
# print a message saying they'll have to wait for a table
# otherwise, report that their table is ready

seating = input("How many people are in your dinner group? ")
seating = int(seating)

if seating >= 8:
    print("\nSorry, you'll have to wait for a table.")
else:
    print("\nYour table is ready.")

# exercise 7-3. multiples of ten
# ask the user for a number
# report whether the number is a multiple of 10 or not

ten = input("Give me a number and I'll tell you if it's a multiple of 10. ")
ten = int(ten)

if ten % 10 == 0:
    print("\nYour number is a multiple of ten.")
else:
    print("\nSorry, try again.")


