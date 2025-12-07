from django.urls import path
from .views import AuthorListCreate, BookListCreate

urlpatterns = [
    path('authors/', AuthorListCreate.as_view()),
    path('books/', BookListCreate.as_view()),
]

