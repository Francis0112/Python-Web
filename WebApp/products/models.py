from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True, max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    summary = models.TextField(max_length=40, default="summary...")
    avail = models.BooleanField(default=False)


class Cars(models.Model):
    brand = models.CharField(max_length=120)
    drive = models.CharField(max_length=120)
    fuel = models.CharField(max_length=120)
    mileage = models.CharField(max_length=120)
    owner = models.CharField(max_length=120)
    active = models.BooleanField(default=False)