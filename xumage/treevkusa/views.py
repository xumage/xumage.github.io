from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def delivery(request):
    return render(request, 'delivery.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def sales(request):
    return render(request, 'sales.html')
