from datetime import datetime
from django.shortcuts import render, redirect ,HttpResponse
from .models import Book  
from django.http import FileResponse
from django.core import serializers
from django.shortcuts import render
from django.http import FileResponse
from .models import *


# Create your views here.



def home(request):
        books = Book.objects.all()
    
        if books:
            print ('working')
    
        context = {
        'books': books,
        }
    
        return render(request, 'index.html', context)

def add_books(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            author = request.POST.get('author')
            genre = request.POST.get('genre')
            publication_year = request.POST.get('publication_year')
            publisher = request.POST.get('publisher')
            isbn = request.POST.get('isbn')
            
            publication_date = datetime(year=int(publication_year), month=1, day=1)

            Book.objects.create(
                title=title, 
                author=author, 
                genre=genre, 
                publisher=publisher, 
                isbn=isbn, 
                publication_date=publication_date, 
                )

            return redirect('/home')  # Redirect to the books page after adding a book

def download_book(request, book_id):
    books = Book.objects.get(pk=book_id)
    file_path = books.book_file.path
    return FileResponse(open(file_path, 'rb'))
        