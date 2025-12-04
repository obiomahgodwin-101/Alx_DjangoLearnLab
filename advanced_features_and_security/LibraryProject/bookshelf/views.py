from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# This view must be named exactly "book_list" and use the permission_required decorator
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

