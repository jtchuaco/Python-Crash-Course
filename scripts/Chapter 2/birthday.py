# avoiding type errors with the str() function
age = 23
message = "Happy " + age + "rd Birthday!"
# this one is an error because Python can't combine str and int, so have to use str()
print(message)

# correct solution
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# exercise 2-8. Number Eight
# write addition, subtraction, multiplication, and division operations that each result in the number 8

# addition
print(5 + 3)

# subtraction
print(12 - 4)

# multiplication
print(4 * 2)

# division
print (16 / 2)

# exercise 2-9. Favorite Number
# store your favorite number in a variable
# using that variable, create a message that reveals your favorite number, and print that message
fav_num = 7
message = "My favorite number is " + str(fav_num) + "."
print(message)