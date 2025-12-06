from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=18)  # default ensures migrations pass

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Default description")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

