from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'advanced_api_project.api'

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        app_label = 'advanced_api_project.api'

