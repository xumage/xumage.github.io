from .models import *

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

def add_user(name, phone_number, email, password):
    user = Users( full_name = name, phone_number = phone_number, email = email, password_hash = password)
    user.save()

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