from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation ---
# Create Authors
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

# Create Books
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(title="Harry Potter", author=author2)

# Create Library
library1 = Library.objects.create(name="Central Library")
library1.books.set([book1, book2, book3])  # Add books to library

# Create Librarian
librarian1 = Librarian.objects.create(name="Alice", library=library1)

# --- Sample Queries ---

# 1. Query all books by a specific author
orwell_books = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:")
for book in orwell_books:
    print(f"- {book.title}")

# 2. List all books in a library
central_books = library1.books.all()
print(f"\nBooks in {library1.name}:")
for book in central_books:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
library_librarian = library1.librarian
print(f"\nLibrarian for {library1.name}: {library_librarian.name}")

