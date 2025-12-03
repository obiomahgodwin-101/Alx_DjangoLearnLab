from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

from .models import Author, Book


@permission_required('relationship_app.view_author', raise_exception=True)
def author_list(request):
    authors = Author.objects.all()
    data = {"authors": list(authors.values("id", "name", "age"))}
    return JsonResponse(data)


@permission_required('relationship_app.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    data = {"books": list(books.values("id", "title", "published_date", "author_id"))}
    return JsonResponse(data)


@permission_required('relationship_app.view_book', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = {
        "id": book.id,
        "title": book.title,
        "published_date": book.published_date,
        "author": book.author.name,
    }
    return JsonResponse(data)

