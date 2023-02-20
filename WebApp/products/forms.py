from django import forms
from .models import Products
from .models import Cars

class ProductsForms(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'txtbox1'}))
	desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	price = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	summary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	# avail = forms.BooleanField()
	class Meta:
		model = Products
		fields = '__all__'


class CarsForms(forms.ModelForm):
	brand = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	drive = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	fuel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	mileage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	owner = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'txtbox1'}))
	# active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
	class Meta:
		model = Cars
		fields= '__all__'

class CircleForm(forms.Form):
	radius = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'txtbox2'}))