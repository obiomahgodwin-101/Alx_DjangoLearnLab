from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# List-only view (kept from previous task)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

