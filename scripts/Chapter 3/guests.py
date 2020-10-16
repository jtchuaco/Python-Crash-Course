# exercise 3-4. guest list
# make a list that includes at least three people you'd like to invite for dinner
# print a message to each person, inviting them to dinner

guest_list = ['Mark', 'Nicole', 'Kaye', 'Ino']

print("Dear " + guest_list[0] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[2] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[3] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")

# exercise 3-5. changing guest list
# add a print statement at the end of your program stating the name of the guest who can't make it

guest_list = ['Mark', 'Nicole', 'Kaye', 'Ino']

print("Dear " + guest_list[0] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[2] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[3] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")

print("Unfortunately, " + guest_list[-1] + " can't make it tonight.")

# modify the list, replace Ino with a new guest

guest_list[-1] = 'Cecile'
print(guest_list)

# print a second set of invitation messages

print("Dear " + guest_list[0] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[2] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[3] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")

# exercise 3-6. more guests
# add a print statement informing people that you found a bigger dinner table

guest_list = ['Mark', 'Nicole', 'Kaye', 'Ino']

print("Dear " + guest_list[0] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[2] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[3] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")

print("Unfortunately, " + guest_list[-1] + " can't make it tonight.")

guest_list[-1] = 'Cecile'
print(guest_list)

print("Hi " + guest_list[0] + "," + "\nJust want to tell you I found a bigger table. \nSee you tonight. \nJudy")
print("Hi " + guest_list[1] + "," + "\nJust want to tell you I found a bigger table. \nSee you tonight. \nJudy")
print("Hi " + guest_list[2] + "," + "\nJust want to tell you I found a bigger table. \nSee you tonight. \nJudy")
print("Hi " + guest_list[3] + "," + "\nJust want to tell you I found a bigger table. \nSee you tonight. \nJudy")

# use insert() to add one new guest to the beginning of your list

guest_list.insert(0, 'HJ')

# use insert() to add one new guest to the middle of your list

guest_list.insert(3, 'Jon')

# use append() to add one new guest to the end of your list

guest_list.append('Jonats')

# print new set of invitation messages, one for each person in your list

print("Dear " + guest_list[0] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[2] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[3] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[4] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[5] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[6] + ',' + "\nYou are cordially invited to dinner at 8pm. \nHope to see you tonight. \nJudy")

# exercise 3-7. Shrinking Guest List
# print a message saying that you can invite only two people for dinner

sorry = "\nI'm so sorry. \nI can't invite you to dinner. \nJudy"

# use pop() to remove guests from your list one at a time until only two names remain.
# each time you pop a name, print a message letting them know you're sorry you can't invite them

guest_list = ['HJ', 'Mark', 'Nicole', 'Jon', 'Cecile', 'Kaye', 'Jonats']
sorry = "\nI'm so sorry. \nI can't invite you to dinner. \nJudy"

guest_list_1 = guest_list.pop()
print("Hi " + guest_list_1 + "," + sorry)
print(guest_list)

guest_list_2 = guest_list.pop()
print("Hi " + guest_list_2 + "," + sorry)
print(guest_list)

guest_list_3 = guest_list.pop()
print("Hi " + guest_list_3 + "," + sorry)
print(guest_list)

guest_list_4 = guest_list.pop()
print("Hi " + guest_list_4 + "," + sorry)
print(guest_list)

guest_list_5 = guest_list.pop()
print("Hi " + guest_list_5 + "," + sorry)
print(guest_list)

# print a message to each of the two people still on your list, letting them know they're still invited
print("Dear " + guest_list[0] + ',' + "\nYou are still invited to dinner. \nHope to see you tonight. \nJudy")
print("Dear " + guest_list[1] + ',' + "\nYou are still invited to dinner. \nHope to see you tonight. \nJudy")

# use del to remove the last two names from your list, so you have an empty list
del guest_list[1]
del guest_list[0]
print(guest_list)



