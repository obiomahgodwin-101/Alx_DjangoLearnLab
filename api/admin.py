from django.contrib import admin
from .models import Author, Book

# Registering Author and Book models so they appear in Django admin.
admin.site.register(Author)
admin.site.register(Book)

