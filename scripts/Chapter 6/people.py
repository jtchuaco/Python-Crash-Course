# exercise 6-7. people
# start with the program you wrote in exercise 6-1
person = {
    'first_name': 'Sean',
    'last_name': 'Tiu',
    'age': 24,
    'city': 'Manila',
}

# make two new dictionaries representing different people
person_1 = {
    'first_name': 'Mark',
    'last_name': 'Herrera',
    'age': 28,
    'city': 'Valenzuela',
}
person_2 = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 17,
    'city': 'London',
}

# store all three dictionaries in a list called people
people = [person, person_1, person_2]

# loop through the list and print everything you know about each person
for persons in people:
    print(persons)

# exercise 6-8. pets
# make several dictionaries,
# where the name of each dictionary is the name of a pet
# in each dictionary, include the kind of animal and the owner's name
hedwig = {'type': 'owl', 'owner': 'harry'}
sky = {'type': 'dog', 'owner': 'lizette'}
crookshanks = {'type': 'cat', 'owner': 'hermione'}
buckbeak = {'type': 'hippogriff', 'owner': 'hagrid'}

# store these dictionaries in a list called pets
pets = [hedwig, sky, crookshanks, buckbeak]

# loop through your list
# print everything you know about each pet
for pet in pets:
    print(pet)

# exercise 6-9. favorite places
# make a dictionary called favorite_places
# think of three names to use as keys in the dictionary
# store one to three favorite places for each person
favorite_places = {
    'sean': ['japan', 'south korea', 'hong kong'],
    'nicole': ['japan', 'sweden'],
    'mark': ['japan', 'UK'],
}
# loop through the dictionary
# print each person's name and their favorite places
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())

# exercise 6-10. favorite numbers
# modify your program in exercise 6-2
# so that each person can have more than one favorite number
favorite_numbers = {
    'kaye': [7, 24],
    'nicole': [3, 22],
    'neil': [16, 10, 20],
    'sean': [17, 11],
    'jd': [7, 14],
}
# print each person's name along with their favorite numbers
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))

# exercise 6-11. cities
# make a dictionary called cities
# use the name of three cities as keys
# create a dictionary of information about each city and the country the city is in
# keys in the city's dictionary should be country, population and fact
cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'It was originally a Roman City called Lutetia',
    },
    'seoul': {
        'country': 'south korea',
        'population': '9.7 million',
        'fact': 'Its official name is Seoul Special Metropolitan City',
    },
    'tokyo': {
        'country': 'japan',
        'population': '9.2 million',
        'fact': 'It was formerly known as Edo in the 20th century',
    },
}
# print the name of each city and all of the information you have stored about it
for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("\tCountry: " + country.title())
    print("\tPopulation: " + population)
    print("\tFact: " + fact + ".")

# exercise 6-12. extensions
# use one of the example programs from this chapter
# extend it by adding new keys and values
# change the context of the program or improve the formatting of the output
# original program
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# extended and change in formatting
players = {
    'efermi': {
        'first_name': 'enrico',
        'last_name': 'fermi',
    },
    'kcrdrf': {
        'first_name': 'mark',
        'last_name': 'herrera',
    },
    'hpotter': {
        'first_name': 'harry',
        'last_name': 'potter',
    },
}

for player, player_info in players.items():
    print("\nPlayer: " + player)
    full_name = player_info['first_name'] + " " + player_info['last_name']

    print("\tThe player's full name is " + full_name.title() + ".")