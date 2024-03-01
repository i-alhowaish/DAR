from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput,EmailInput
from .models import *
from django import forms
'''
# This how in Django Course Video he made the User record

class CreateUserFrom(UserCreationForm):
  
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


'''



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(widget=TextInput(),max_length=15,required=False)
   

    class Meta:
        model = User
        fields = ["username", "password1","password2", "first_name", "last_name", "email", "phone_number"]

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['description', 'type', 'price', 'furnished', 'number_of_bathrooms', 'region', 'city', 'street', 
                  'neighborhood', 'coordinate', 'length', 'width', 'number_of_sides', 'number_of_rooms', 
                  'sell_or_rent', 'number_of_parkings', 'number_of_bedrooms', 'year_built']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class PropertyImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields = ['image']
        #'multiple': True,
        widgets = {
            'image': forms.FileInput(attrs={ 'accept': 'image/jpeg,image/png,image/jpg'}),
        }


class PropertyImages360Form(forms.ModelForm):
    class Meta:
        model = PropertyImages360
        fields = ['image360']
        #'multiple': True,
        widgets = {
            'image360': forms.FileInput(attrs={ 'accept': 'image/jpeg,image/png,image/jpg'}),
        }



class updatePropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'description', 'type', 'price', 'furnished', 'number_of_bathrooms',
            'region', 'city', 'street', 'neighborhood', 'coordinate', 'length', 
            'width', 'number_of_sides', 'number_of_rooms', 'sell_or_rent', 
            'number_of_parkings', 'number_of_bedrooms', 'year_built'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'type': forms.Select(),
            'price': forms.NumberInput(),
            'furnished': forms.CheckboxInput(),
            'number_of_bathrooms': forms.NumberInput(),
            'region': forms.Select(),
            'city': forms.Select(),
            'street': forms.TextInput(),
            'neighborhood': forms.Select(),
            'coordinate': forms.TextInput(),
            'length': forms.NumberInput(),
            'width': forms.NumberInput(),
            'number_of_sides': forms.NumberInput(),
            'number_of_rooms': forms.NumberInput(),
            'sell_or_rent': forms.Select(),
            'number_of_parkings': forms.NumberInput(),
            'number_of_bedrooms': forms.NumberInput(),
            'year_built': forms.NumberInput(),
        }