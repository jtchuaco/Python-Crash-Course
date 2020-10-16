# organizing a list
# using sort() method
# better if the values in the list is in lowercase when sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort by passing the argument reverse=True
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# using the sorted() function, you can maintain the original order of a list but present it in sorted order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# using the reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# finding the length of a list
# using the len() function
# python counts the items in a list starting with one when determining the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

