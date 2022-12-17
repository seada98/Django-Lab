from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300 , null=True)
    price = models.IntegerField(default=100)

    def __str__(self):
      return f"{self.name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300 , null=True)
    price = models.IntegerField(default=100)

    def __str__(self):
      return f"{self.name}"
