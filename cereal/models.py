from django.db import models

class CerealCategory(models.Model):
    name = models.CharField(max_length=255)

class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(CerealCategory,on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()

class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    candy = models.ForeignKey(Cereal, on_delete=models.CASCADE())
# Create your models here.
