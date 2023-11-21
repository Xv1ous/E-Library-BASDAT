from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, default='Unknown')
    isbn = models.IntegerField(default=1111111111111)
    publication_year = models.DateField()
