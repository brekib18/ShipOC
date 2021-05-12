from django.db import models

# Create your models here.
from django.db import models
from frontpage.models import Category

from auth_user import id


class CartCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = id

    def __str__(self):
        return self.name


class CartImage(models.Model):
    image = models.CharField(max_length=9999)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

