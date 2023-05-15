from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=20)


class Orders(models.Model):
    user_phone_number = models.CharField(max_length=20)


class FoodMenu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    weight = models.IntegerField()
    price=models.IntegerField()
    image_path = models.CharField(max_length=300)
    type = models.CharField(max_length=100)