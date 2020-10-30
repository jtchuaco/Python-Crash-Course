# exercise 5-1. Conditional Tests
# write a series of conditional tests
# print a statement describing each test
# and your prediction for the results of each test
# create at least 10 tests
# 5 tests evaluate to True
# 5 tests evaluate to False

stationery = 'stickers'
print("Is stationery == 'stickers'? I predict True.")
print(stationery == 'stickers')

print("\nIs stationery == 'paper'? I predict False.")
print(stationery == 'paper')

print("\nIs stationery != 'washi tape'? I predict True.")
print(stationery != 'washi tape')

print("\nIs stationery != 'stickers'? I predict False.")
print(stationery != 'stickers')

chinese_food = 'siomai'
print("Is chinese_food == 'siomai'? I predict True.")
print(chinese_food == 'siomai')

print("\nIs chinese_food != 'siopao'? I predict True.")
print(chinese_food != 'siopao')

print("\nIs chinese_food == 'beijing duck'? I predict False.")
print(chinese_food == 'beijing duck')

weather = 'gloomy'
print("Is weather == 'rainy'? I predict False.")
print(weather == 'rainy')

print("\nIs weather != 'gloomy'? I predict False.")
print(weather != 'gloomy')

print("\nIs weather != 'cloudy'? I predict True.")
print(weather != 'cloudy')

# exercise 5-2. More Conditional Tests
# tests for equality and inequality with strings
blackpink_member = 'Rose'
blackpink_member == 'Rose'
print("Yes, she is.")

blackpink_member == 'Dara'
print("No, she's not.")

# tests using the lower() function
kpop_boygroup = 'BTS'
kpop_boygroup.lower == 'bts'
print("Yey, it's a match.")

# numerical tests involving equality and inequality
# greater than and less than
# greater than or equal to and less than or equal to
lucky_number = 7
if lucky_number == 7:
    print("That's right! It is 7.")

if lucky_number != 14:
    print("Try again.")

if lucky_number > 5:
    print("Yes.")

if lucky_number < 10:
    print("Yes.")

if lucky_number >= 7:
    print("Yes.")

if lucky_number <= 14:
    print("Yes.")

# tests using the and keyword and the or keyword
Anna_age = 21
Betty_age = 23

Anna_age > 18 and Betty_age < 30
print("Pass. You may enter.")

Anna_age <= 10 or Betty_age >= 20
print("Betty passes.")

# test whether an item is in a list
flavors = ['chocolate', 'strawberry', 'pistachio']

'chocolate' in flavors
print("Yes.")

# test whether an item is not in a list
dimsum = ['siomai', 'siopao', 'hakaw']

'radish cake' not in dimsum
print("Yes.")
