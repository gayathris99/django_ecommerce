from django.db import models 
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255 , unique=True)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, unique=True)
    description = models.TextField(blank = True , null = True)
    price = models.FloatField()

    def __str__(self):
        return self.title 
