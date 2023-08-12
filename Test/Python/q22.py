# Q22. Create an empty dictionary called ages. Add the following key-value pairs to the dictionary:
# "Alice": 30
# "Bob": 25
# "Charlie": 35
# Then, print out the age of Charlie.
ages = {}
ages_update = {"Alice": 30,
               "Bob": 25,
               "Charlie": 35}
ages.update(ages_update)
print(ages)