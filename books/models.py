from django.db import models
class BooksCategory(models.Model):
    name = models.CharField(max_length=255)

class Books(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    category = models.ForeignKey(BooksCategory,on_delete=models.CASCADE)
    price = models.FloatField()

class BooksImage(models.Model):
    image = models.CharField(max_length=9999)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)