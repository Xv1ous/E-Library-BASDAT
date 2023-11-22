from django.urls import path
from . import views 
from .views import download_book

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('add_books/', views.add_books, name='add_books'),
    path('books/download/<int:book_id>/', download_book, name='download_book'),
    
]