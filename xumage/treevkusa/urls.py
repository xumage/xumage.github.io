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
    path('register/', views.register, name='register')
]
