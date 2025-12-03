from django.db import models

# ----------------------------------
#  Book Model
# ----------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

