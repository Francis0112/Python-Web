from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    avail = models.BooleanField(default=False)
    summary = models.TextField(default="item summary...")


class Cars(models.Model):
    brand = models.CharField(max_length=120)
    drive = models.CharField(max_length=120)
    fuel = models.CharField(max_length=120)
    mileage = models.CharField(max_length=120)
    owner = models.CharField(max_length=120)
    active = models.BooleanField(default=False)
