# Q19. favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
# favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
# Use the zip() function to combine the book set and movie list into a list of tuples representing
# book movie pairs. Print the resulting list.
favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]

items = zip(favorite_books, favorite_movies)
for item in items:
    print(item)