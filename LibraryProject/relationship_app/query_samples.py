from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def books_in_library(library_name):
    return Book.objects.filter(library__name=library_name)

def librarian_of_library(library_name):
    librarian = Librarian.objects.filter(library__name=library_name).first()
    return librarian.name if librarian else None

