from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book model.
# Serializes all fields and includes custom validation.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        """
        Custom validation:
        Ensures a book cannot be created with a future publication year.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'


# AuthorSerializer includes a nested list of books using the BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer showing all books belonging to the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

