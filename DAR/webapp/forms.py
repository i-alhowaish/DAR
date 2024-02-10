from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


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
