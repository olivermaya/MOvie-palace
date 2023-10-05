from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile

class RegisterUserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =['username','email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']
    