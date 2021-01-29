# exercise 8-1. message
# write a function called display_message()
# that prints one sentence telling everyone what you are learning about in this chapter
# call the function
# make sure the message displays correctly

def display_message():
    """What are you learning about in this chapter."""
    print("I'm learning about functions in this chapter.")

display_message()

# exercise 8-2. favorite book
# write a function called favorite_book()
# that accepts one parameter, title
# the function should print a message
# call the function,
# make sure to include a book title as an argument in the function call

def favorite_book(title):
    """What is your favorite book?"""
    print("One of my favorite books is " + title.title() + ".")

favorite_book("Harry Potter")



