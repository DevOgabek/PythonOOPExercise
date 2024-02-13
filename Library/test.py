from book import Book
from library import Library

# Creating a library
my_library = Library()

# Adding books to the library
book1 = Book("Book1", "Author1")
book2 = Book("Book2", "Author2")
book3 = Book("Book3", "Author3")

my_library.add(book1, floor=1, shelf=1, closet=1, position=1)
my_library.add(book2, floor=2, shelf=5, closet=3, position=2)
my_library.add(book3, floor=3, shelf=10, closet=5, position=3)

# Checking if books are present
print(my_library.contains(book1))  # Should print the position of Book1
print(my_library.contains(book2))  # Should print the position of Book2
print(my_library.contains(Book("NonexistentBook", "NonexistentAuthor")))  # Should print not found message

# Retrieving book information
my_library.get_books(floor=1, shelf=1, closet=1)  # Should print Book1 information

# Finding books
print(my_library.find(name="Book2", author="Author2"))  # Should print the position of Book2
print(my_library.find(name="NonexistentBook", author="NonexistentAuthor"))  # Should print not found message

# Retrieving location information
print(my_library.get_floor(book2))  # Should print the floor of Book2
print(my_library.get_shelf(book2))  # Should print the shelf of Book2
print(my_library.get_closet(book2))  # Should print the closet of Book2