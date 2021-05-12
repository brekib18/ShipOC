from django.db import models

from django.contrib.auth.models import User

from frontpage.models import Category
# Create your models here.
class CartCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class CartImage(models.Model):
    image = models.CharField(max_length=9999)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
