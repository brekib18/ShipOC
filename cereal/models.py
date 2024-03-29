from django.db import models
from frontpage.models import Category


class CerealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    cereal_category_id = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        a = str(self.cereal_category_id)
        return a


class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal,on_delete=models.CASCADE)