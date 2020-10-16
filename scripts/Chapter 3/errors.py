# avoiding index errors when working with lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcyles[3])
# result is an index error because there is no item in the list that has an index of 3
# remember index starts at 0
# when you want to access the last item, you can always use the index -1
print(motorcycles[-1])
# it will only cause an error if you request the last item from an empty list
motorcycles = []
print(motorcycles[-1])

# exercise 3-11. intentional error.
journals = ['stationery', 'notebook', 'washitape', 'stamps']
print(journals[4])
# correct index error
print(journals[-1])