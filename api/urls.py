from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view()),
    path('books/', views.BookListCreateView.as_view()),
]

