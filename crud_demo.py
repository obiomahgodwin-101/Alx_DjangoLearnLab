import os
import django

# 1. Point to your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# 2. Setup Django
django.setup()

# 3. Import models after setup
from bookshelf.models import Book

# CREATE
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print("Created book:", book)

# RETRIEVE
books = Book.objects.all()
print("All books:", books)

# UPDATE
book.title = "Nineteen Eighty-Four"
book.save()
print("Updated book:", book)

# DELETE
book.delete()
print("Deleted book. Remaining books:", Book.objects.all())

