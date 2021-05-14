
# Create your models here.
from django.db import models
from frontpage.models import Category


class AccessoriesCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()


class AccessoriesImage(models.Model):
    image = models.CharField(max_length=9999)
    accessories = models.ForeignKey(Accessories,on_delete=models.CASCADE)