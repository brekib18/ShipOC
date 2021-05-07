from django.db import models
class ClothesCategory(models.Model):
    name = models.CharField(max_length=255)

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    category = models.ForeignKey(ClothesCategory,on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()

class ClothesImage(models.Model):
    image = models.CharField(max_length=9999)
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE)