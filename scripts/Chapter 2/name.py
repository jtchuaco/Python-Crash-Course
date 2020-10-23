# adding method to a string
name = "ada lovelace"

# title() is where each word begins with a capital letter
print(name.title())

# upper() is capitalize everything
print(name.upper())

# lower() is lowercase everything. useful for storing data
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# combining strings or concatenating strings
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# adding whitespace to strings with tabs or newlines
# whitespace refers to nonprinting character like space,tabs,etc
print("Python")

# tabs = \t
print("\tPython")

# newlines = \n
print("Languages:\nPython\nC\nJavaScript")

# combine tabs and newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespace
# rstrip() - right end of a string
# lstrip() - left end of a string
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
print(favorite_language)
