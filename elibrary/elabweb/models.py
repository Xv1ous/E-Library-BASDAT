from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, default='Unknown')
    isbn = models.CharField(max_length=15)
    publication_year = models.DateField()
    Amount = models.CharField(max_length=100)
    book_file = models.FileField(upload_to='book_files/',null=True)
    
    def __str__(self):
        return self.title   
