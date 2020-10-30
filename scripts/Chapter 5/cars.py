# if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # checks if the current value of car is 'bmw'
    if car == 'bmw':
        # if yes, then print value in uppercase
        print(car.upper())
    else:
        print(car.title())

# conditional tests
# evaluates if statement as True or False
# compare the current value of variable to a specific value of interest

# checking for equality (==)
# sets the value of car to 'bmw' using a single equal sign
car = 'bmw'
# checks whether the value of car is 'bmw' using ==
# double equal sign (==) or equality operator
car == 'bmw'

# remember: testing for equality is case sensitive in Python
car = 'Audi'
# can always use the lower() function when checking
car.lower() == 'audi'






