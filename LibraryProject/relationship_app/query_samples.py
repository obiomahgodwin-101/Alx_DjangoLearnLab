from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation ---
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(title="Harry Potter", author=author2)

library1 = Library.objects.create(name="Central Library")
library1.books.set([book1, book2, book3])

librarian1 = Librarian.objects.create(name="Alice", library=library1)

# --- Sample Queries as expected by checker ---

# 1. Query all books by a specific author
author_name = "George Orwell"
orwell_books = Author.objects.get(name=author_name).books.all()
print(f"Books by {author_name}:")
for book in orwell_books:
    print(f"- {book.title}")

# 2. List all books in a library
library_name = "Central Library"
library_books = Library.objects.get(name=library_name).books.all()
print(f"\nBooks in {library_name}:")
for book in library_books:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
library_librarian = Library.objects.get(name=library_name).librarian
print(f"\nLibrarian for {library_name}: {library_librarian.name}")

