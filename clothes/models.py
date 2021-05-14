from django.db import models
from frontpage.models import Category

class ClothesCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()

class ClothesImage(models.Model):
    image = models.CharField(max_length=9999)
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE)