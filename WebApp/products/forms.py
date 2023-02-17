from django import forms
from .models import Products
from .models import Cars


class ProductsForms(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
	price = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# avail = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
	summary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Products
		fields = '__all__'


class CarsForms(forms.ModelForm):
	brand = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	drive = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	fuel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mileage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	owner = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
	class Meta:
		model = Cars
		fields= '__all__'