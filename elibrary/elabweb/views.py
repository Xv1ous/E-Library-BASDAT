from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def save_name(request):
    name = request.POST.get('name')
    return HttpResponse("Welcome " + name + "!")