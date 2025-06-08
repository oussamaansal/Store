from django.db import models
from django.contrib.auth.models import AbstractUser


class User_one(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
