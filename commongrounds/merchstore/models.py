from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


# Create your models here.
