
# Create your models here.
from django.db import models


class AccessoriesCategory(models.Model):
    name = models.CharField(max_length=255)


class Accessories(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    category = models.ForeignKey(AccessoriesCategory,on_delete=models.CASCADE)
    price = models.IntegerField()


class AccessoriesImage(models.Model):
    image = models.CharField(max_length=9999)
    accessories = models.ForeignKey(Accessories,on_delete=models.CASCADE)