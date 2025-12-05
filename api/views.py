from rest_framework import viewsets
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# ListAPIView for Authors
class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# ViewSet for Book model with full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

