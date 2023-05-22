from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .crud import *
import requests

def add_item_to_cart(request):
    food_name = request.POST.get("name")
    print(request.session["cart"])
    if request.session['cart'] != {}:
        data = request.session["cart"]["items"]
        data.append(get_food(food_name))
        request.session["cart"] = {"items": data}
    else:
        request.session['cart'] = {'items': []}
        request.session["cart"] = {"items": [get_food(food_name)]}
    
    
    total_price = 0
    for i in request.session["cart"]["items"]:
        total_price += i["price"]
    request.session['cart']['total_price'] = total_price

        
    return HttpResponseRedirect("/")

def send_notification(request):
    if request.POST.get('task') == 'Заказать':
        items = request.session['cart']['items']
        tp = request.session['cart']['total_price']
        text = ''
        for i in items:
            text = text + (i['name'] + "-" + str(i['price']) + "\n")
        text += f'Итоговая стоимость: {tp}' 
        requests.get(f"https://api.telegram.org/bot5615049869:AAGP8kegIbPgms30ep0GTT6nDwadeUzc5uw/sendMessage?chat_id=-1001840733210&text={text}")

        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def create_order(request):
    return render(request, 'create_order.html')

def postuser(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_number = request.POST.get('tel')
    password = request.POST.get('password')
    verify_password = request.POST.get('verify_password')
    add_user(name=name, password=password, email=email, phone_number=phone_number)
    del name,email,phone_number,password,verify_password
    return HttpResponseRedirect("/login")

def loginuser(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    tel = request.POST.get('tel')
    if if_user_exist(name, email, tel) == False:
        return HttpResponseRedirect("/login")
    request.session["credentials"] = {"name": name, "email": email, "tel": tel}
    return HttpResponseRedirect("/")

def index_page(request):
    print(request.session.get("cart"))
    data = get_all_foods()
    if request.session.get("credentials"):
        data['credentials'] = request.session.get("credentials")
    return render(request, 'index.html', data)

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