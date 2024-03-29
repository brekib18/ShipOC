from django.db import models
from frontpage.models import Category


class BooksCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name




class Books(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class BooksImage(models.Model):
    image = models.CharField(max_length=9999)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
