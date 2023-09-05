from typing import Any
from django import forms
from .models import Twieet , Supplier
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class TwieetForm(forms.ModelForm):
    body = forms.CharField(required=True ,
             widget=forms.Textarea(attrs={
                 "palceholder":"Enter Your Twieet...!",
                 "class":"form-control"
             }), label="",)
    
    class Meta:
        model = Twieet
        exclude = ("user",)

# Register Form.......................................................
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="User Name" , max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email" , widget=forms.TextInput(attrs={'class':'form-control' }))
    first_name = forms.CharField(label="First Name" ,max_length=100 , widget=forms.TextInput(attrs={'class':'form-control' }))
    last_name = forms.CharField(label="last Name" ,max_length=100 , widget=forms.TextInput( attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    





# Insert Supplier Form..........................................................
# class SupplierForm(forms.ModelForm):
#     supplier_name = forms.CharField(label="" , max_length=100 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Supplier Name'}))
#     jon_size = forms.CharField(label='' , required=True , max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Jon Size'}))
#     jon_price = forms.CharField(label='' , max_length=50 , widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Jon Price' , 'type':'number'}))

#     class Meta:
#         model = Supplier
#         fields = ("supplier_name","jon_size","jon_price")