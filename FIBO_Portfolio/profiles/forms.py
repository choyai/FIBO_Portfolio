from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

    class Meta:
        model = User
        fields = ['username','password']
        widget={
            'username': forms.TextInput(attrs={'class':'input'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'avatar', 'bio']