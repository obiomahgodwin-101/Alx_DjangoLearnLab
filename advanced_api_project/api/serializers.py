from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        # Example: add any custom validation if needed
        return data

# AuthorSerializer with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'books']

