from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    avail = models.BooleanField(default=False)
    summary = models.TextField(default="onegai shi masu")
