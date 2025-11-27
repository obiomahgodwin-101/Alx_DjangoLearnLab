from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print("\nBooks in Central Library:")
for book in library.books.all():
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for Central Library:", librarian.name)

