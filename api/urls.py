from django.urls import path
from .views import BookListCreateView, AuthorListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books'),
    path('authors/', AuthorListCreateView.as_view(), name='authors'),
]

