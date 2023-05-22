from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('sales/', views.sales, name='sales'),
    path('register/', views.register, name='register'),
    path("register/postuser/", views.postuser, name='postuser'),
    path("login/loginuser/", views.loginuser, name='loginuser'),
    path("add-to-cart/", views.add_item_to_cart, name='add_to_cart'),
    path("create-order/", views.create_order, name='create-order'),
    path("create-order/send-notification/", views.send_notification, name='send-notification'),

]


