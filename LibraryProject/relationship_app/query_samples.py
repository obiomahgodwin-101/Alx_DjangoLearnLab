from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_author)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
all_books = library.books.all()
print(f"Books in {library.name}:", all_books)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}:", librarian)

