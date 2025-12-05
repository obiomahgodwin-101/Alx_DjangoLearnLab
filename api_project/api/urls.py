from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path('books/', views.BookList.as_view(), name='book-list'),
]

