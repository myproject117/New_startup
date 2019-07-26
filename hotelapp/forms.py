from django import forms
from .models import Customer
from datetime import datetime

class CustomerForm(forms.ModelForm):
     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
     age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
     phoneno = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
     idproof = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

     class Meta():
        model = Customer
        fields = ('name','age','phoneno','idproof','room','payment_mode','reporting')