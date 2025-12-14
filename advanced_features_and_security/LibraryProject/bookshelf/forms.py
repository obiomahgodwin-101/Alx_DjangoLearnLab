from django import forms
from .models import Book

# ExampleForm as requested in the security task
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'description']

