# Q24. Create a dictionary called phone_book with the following key-value pairs:
# "Alice": "555-1234"
# "Bob": "555-5678"
# "Charlie": "555-9012"
# Then, prompt the user to enter a name and print out the corresponding phone number. If the
# name is not
# in the phone book, print out a message saying that the name was not found.

phone_book = {"Alice": "555-1234",
              "Bob": "555-5678",
              "Charlie": "555-9012"}

name = input('Enter name: ')
if name in phone_book:
    print(phone_book[name])
else:
    print('Name not found')