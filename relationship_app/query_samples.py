import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Clear existing data (optional, for repeated runs)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create sample authors and books
author1 = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="Arrow of God", author=author1)

# Create a library and add books
library1 = Library.objects.create(name="National Library")
library1.books.set([book1, book2])

# Create a librarian
librarian1 = Librarian.objects.create(name="Michael", library=library1)

# Queries
print(f"Books by {author1.name}:")
for book in author1.books.all():
    print(f"- {book.title}")

print(f"Books in {library1.name}:")
for book in library1.books.all():
    print(f"- {book.title}")

print(f"Librarian for {library1.name}: {library1.librarian.name}")

