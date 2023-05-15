from django.shortcuts import render
from django.http import HttpResponse
from treevkusa.models import *

def get_some_data_from_db(food_type: str) -> dict:
    response_json_object: dict = { food_type + 's': [] }

    for food in FoodMenu.objects.all().filter(type=food_type):
        response_json_object[food_type + 's'].append(
            {
                'name': food.name,
                'desc': food.description,
                'weight': food.weight,
                'price': food.price,
                
            }
        )
    print(response_json_object)
    return response_json_object

def get_all_foods() -> dict:
    response_json_object: dict = {}

    for food_type in ['burger', 'hotdog', 'pizza', 'shaurma', 'drink']:
        response_json_object[food_type + 's'] = []
        for food in FoodMenu.objects.all().filter(type=food_type):
            response_json_object[food_type + 's'].append(
                {
                    'name': food.name,
                    'desc': food.description,
                    'weight': food.weight,
                    'price': food.price,
                    'img_path': food.image_path
                }
            )
    print(response_json_object)
    return response_json_object


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
