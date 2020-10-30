# numerical comparisons
answer = 17
# because the value of answer is not equal to 42
# the indented code block is executed
if answer != 42:
    print("That is not the correct answer. Please try again!")

# other numerical comparisons
# < , <=, >, >=
age = 19
age < 21
# True
age <= 21
# True
age > 21
# False
age >= 21
# False
# each mathematical comparison can be used as part of an if statement

# checking multiple conditions
# by using the keywords 'and' and 'or'

# using keyword: 'and'
# if each test passes, then it evaluates to True
# if either test fails or if both tests fail, the expression evaluates to False

# define two ages
age_0 = 22
age_1 = 18

# check whether both ages are 21 or older
# the test on the left passes, but the test on the right fails
age_0 >= 21 and age_1 >= 21
# overall conditional expression evaluates to False

# change age_1 to 22
age_1 = 22

# check whether both ages are 21 or older
# both individual tests pass
age_0 >= 21 and age_1 >= 21
# overall conditional expression evaluates to True


# to improve readability, can use parentheses around the individual tests
# parentheses are not required
# but if you use it, it'll look like
(age_0 >= 21) and (age_1 > 21)


# using keyword: 'or'
# test passes when either or both of the individual test pass
# fails when both individual tests fail

# define two ages
age_0 = 22
age_1 = 18

# check if one person is over 21
age_0 > 21 or age_1 >= 21
# because age_0 passes, overall expression evaluates to True

# lower age of age_0
age_0 = 18

# check if one person is over 21
age_0 >= 21 or age_1 >= 21
# because both tests failed, overall expression evaluates to False


