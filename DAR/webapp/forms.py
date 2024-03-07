from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput,EmailInput
from .models import *
from django import forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate

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


        

class UserSettingsForm(forms.ModelForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(), required=False)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(), required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    color_of_profile = forms.CharField(max_length=7, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, user=None, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        self.user = user
        if self.instance:
            profile, created = UserProfile.objects.get_or_create(user=self.instance)
            self.fields['phone_number'].initial = profile.phone_number
            self.fields['color_of_profile'].initial = profile.color_of_profile

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Your old password was entered incorrectly. Please enter it again.")
        return old_password

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two new password fields didn't match.")
        return new_password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["new_password1"]:
            user.set_password(self.cleaned_data["new_password1"])
        if commit:
            user.save()
        profile = UserProfile.objects.get(user=user)
        profile.phone_number = self.cleaned_data['phone_number']
        profile.color_of_profile = self.cleaned_data['color_of_profile']
        profile.save()
        return user


class userImages(forms.ModelForm):
    class Meta:
        model = userImages
        fields = ['userimage']
        #'multiple': True,
        widgets = {
            'userimage': forms.FileInput(attrs={ 'accept': 'image/jpeg,image/png,image/jpg'}),
        }