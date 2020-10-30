# exercise 4-3. Counting to twenty
# use a for loop to print the numbers from 1 to 20, inclusive
for twenty in range(1, 21):
    print(twenty)

# exercise 4-4. one million
# make a list of the numbers from one to one million, and then use a for loop to print the numbers
millions = list(range(1, 1000001))
print(millions)
for million in millions:
    print(million)

# exercise 4-5. summing a million
# make a list of the numbers from one to one million
# use min() and max() to make sure your list actually starts at one and ends at one million
# use sum() function to see how quickly Python can add a million numbers.
mil = list(range(1, 1000001))
# min()
min(mil)
# max()
max(mil)
# sum()
sum(mil)

# exercise 4-6. odd numbers
# use the third argument of the range() function to make a list of odd numbers from 1 to 20
# use a for loop to print each number
odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
    print(odd)

# exercise 4-7. threes
# make a list of the multiples of 3 from 3 to 30.
# use a for loop to print the numbers in your list
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

# exercise 4-8. cubes
# make a list of the first 10 cubes (the cube of each integer from 1 through 10)
# use a for loop to print out the value of each cube
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
    print(cube)

# exercise 4-9. cube comprehension
# use a list comprehension to generate a list of the first 10 cubes
cubes = [value**3 for value in range(1, 11)]
print(cubes)



