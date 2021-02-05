# exercise 8-6. city names
# write a function called city_country() that takes in the name of a city and country
# call your function with at least three city-country pairs
# print the value that's returned

def city_country(city, country):
    """Return a city and country, neatly formatted."""
    cc_pair = city + ', ' + country
    return cc_pair.title()

favorite_place = city_country('seoul', 'south korea')
print(favorite_place)

favorite_place = city_country('tokyo', 'japan')
print(favorite_place)

favorite_place = city_country('london', 'united kingdom')
print(favorite_place)

# exercise 8-7. album
# write a function called make_album() that builds a dictionary describing a music album
# should have artist name and album title
# should return a dictionary containing these two pieces of information
# make three dictionaries representing different albums
# print each return value to show that the dictionaries are storing the album correctly

def make_album(artist_name, album_name):
    """Return a dictionary of information about an album."""
    record = {'artist': artist_name.title(), 'album': album_name.title()}
    return record

playlist = make_album('taylor swift', '1987')
print(playlist)

playlist = make_album('blackpink', 'the album')
print(playlist)

playlist = make_album('spice girls', 'spiceworld')
print(playlist)

# add an optional parameter that allows you to store the number of tracks on an album
# if the calling line includes a value for the number of tracks, add that value to the album's dictionary
# make at least one new function call that includes the number of tracks on an album

def make_album(artist_name, album_name, track=''):
    """Return a dictionary of information about an album."""
    record = {'artist': artist_name.title(), 'album': album_name.title()}
    if track:
        record['track'] = track
    return record

playlist = make_album('taylor swift', '1987')
print(playlist)

playlist = make_album('blackpink', 'the album')
print(playlist)

playlist = make_album('spice girls', 'spiceworld')
print(playlist)

playlist = make_album('backstreet boys', 'backstreet boys', '13')
print(playlist)

# exercise 8-8. user albums
# start with your program from exercise 8-7
# write a while loop that allows users to enter an album's artist and title
# call make_album() with the user's input and print the dictionary
# be sure to include a quit value

def make_album(artist_name, album_name):
    """Return a dictionary of information about an album."""
    record = {'artist': artist_name.title(), 'album': album_name.title()}
    return record

while True:
    print("\nPlease enter the artist and album name:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    playlist = make_album(artist_name, album_name)
    print(playlist)



