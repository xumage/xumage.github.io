from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .crud import *

def postuser(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_number = request.POST.get('tel')
    password = request.POST.get('password')
    verify_password = request.POST.get('verify_password')
    add_user(name=name, password=password, email=email, phone_number=phone_number)
    del name,email,phone_number,password,verify_password
    return HttpResponseRedirect("/login")

def index_page(request):
    return render(request, 'index.html', get_all_foods())

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

def register(request):
    return render(request, 'reg.html')