# exercise 2-7. stripping names
# store a person's name, and include some whitespace characters at the beginning and end of the name
# use each character combination, "\t" and "\n", at least once
# print the name once to have the whitespace displayed and then print the name using each of the three strip functions
name_2 = " judy "
print(name_2)

name_2 = name_2.rstrip()
print(name_2)

name_2 = name_2.lstrip()
print(name_2)

name_2 = name_2.strip()
print(name_2)

name_3 = "\tJudy"
name_4 = name_3.strip()
print(name_4)

name_5 = "Judy\n"
name_6 = name_5.rstrip()
print(name_6)

name_7 = "\t\nJudy "
name_8 = name_7.lstrip()
print(name_8)

# exercise 2-8. Stripping strings
# using only python's strip function, strip the following strings in order to print out the expected output

one = "I saw Myrtle crying yesterday."
# expected output: "I saw Myrtle crying yesterday"
one_answer = one.rstrip('.')
print(one_answer)

two = "$$$ This dog is very friendly."
# expected output: "This dog is very friendly."
two_answer = two.lstrip('$$$ ')
print(two_answer)

three = "$$$ This dog is very friendly."
# expected output: "This dog is very friendly"
three_answer = three.strip('$$$ ')
three_answer_1 = three_answer.rstrip('.')
print(three_answer_1)

four = "Php 29.99"
# expected output: "29.99"
four_answer = four.strip('Php ')
print(four_answer)

five = "\t \n 1+1=2"
# expected output: "1+1=2"
five_answer = five.lstrip()
print(five_answer)

six = "\n This is a new line. \n \t"
# expected output: "This is a new line."
six_answer = six.strip()
print(six_answer)

seven = "\n This is a new line. \t This is a new tab. \t"
# expected output: "This is a new line. \t This is a new tab."
seven_answer = seven.strip()
print(seven_answer)
# i'm not sure how to maintain the \t at the middle of the sentences. Help please.

eight = "?? How many hours did it rain yesterday?"
# expected output: "How many hours did it rain yesterday?"
eight_answer = eight.lstrip('?? ')
print(eight_answer)

# exercise 2-9. Strip Question
# Question 1: Explain the difference of strip, rstrip, and lstrip.
# Answers:
# strip is removing the whitespace from the start and end of the string
# rstrip is removing the whitespace that exists from the right end of a string
# lstrip is removing the whitespace that exists from the left end of a string

# Question 2: For the text "$$ Money makes the world go round.", how many times do I need to use .lstrip("$") in order
# to get "Money makes the world go round."
# The answer is just 1 time.

answer = "$$ Money makes the world go round."
answer = answer.lstrip('$ ')
print(answer)


