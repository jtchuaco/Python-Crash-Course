# exercise 3-1. Names
# store the names of your friends in a list
# print each person's name by accessing each element in the list, one at a time
names = ['Mark', 'Nicole', 'Kaye', 'Ino', 'Jon']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

# exercise 3-2. Greetings
# using the list you created, print a message to them.
message0 = "How are you doing, " + names[0] + "?"
message1 = "How are you doing, " + names[1] + "?"
message2 = "How are you doing, " + names[2] + "?"
message3 = "How are you doing, " + names[3] + "?"
message4 = "How are you doing, " + names[-1] + "?"
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)

# exercise 3-3. Your own list
# make a list of your favorite mode of transportation and print a series of statements about it
transportation = ['car', 'airplane', 'bicycle']
print("My dream " + transportation[0] + " is a Hyundai Tucson.")
print("Whenever I travel, one thing I always look forward to is eating " + transportation[1] + " food.")
print("I'm not sure if I can still ride a " + transportation[-1] + ".")

