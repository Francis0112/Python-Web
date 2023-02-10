from django import forms
from .models import Products
from .models import Cars

class ProductsForms(forms.ModelForm):
	class Meta:
		model = Products
		fields = [
			"name",
			"desc",
			"price",
			"avail",
			"summary"
		]

class CarsForms(forms.ModelForm):
	class Meta:
		model = Cars
		fields=[
			"brand",
		    "drive",
		    "fuel", 
		    "mileage",
		    "owner",
		    "active"
		]	