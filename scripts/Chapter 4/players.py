# working with part of a list
# slicing a list
# to make a slice, specify the index of the first and last elements you want to work with
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# prints a slice of the list, which includes just the first three players
print(players[0:3])
# if you want the second, third, fourth items, start the slice at index 1 and end at index 4
print(players[1:4])
# if you omit the first index in a slice, python automatically starts your slice at the beginning of the list
print(players[:4])
# slice that includes the end of a list
print(players[2:])
# slice using negative index
print(players[-3:])

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
# only loop through the first three names
for player in players[:3]:
    print(player.title())

