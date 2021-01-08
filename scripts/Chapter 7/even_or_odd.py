# the modulo operator (%)
# divides one number by another number and returns the remainder

4 % 3

5 % 3

6 % 3

7 % 3

# when one number is divisible by another number,
# the remainder is 0
# so the modulo operator always returns 0
# use this fact to determine if a number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# even numbers are always divisible by two
# so if the modulo of a number and two is zero, the number is even
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

