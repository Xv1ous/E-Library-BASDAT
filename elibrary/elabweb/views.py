from datetime import datetime
from django.shortcuts import render, redirect ,HttpResponse
from .models import Book  

    # Create your views here.
def home(request):
        return render(request, 'index.html')

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

        # Render the form if the request method is not POST
        return render(request, 'add_books.html')
    
def book_list(request):
   books = Book.objects.all()
   return render(request, 'book_list.html', {'books': books})

# def Download_Books(request):
#     for book in Book.objects.all():
        