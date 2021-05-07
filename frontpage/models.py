from django.db import models
class category(models.Model):
    name = models.CharField(max_length=255)

class CategoryImage(models.Model):
    image = models.CharField(max_length=9999)
