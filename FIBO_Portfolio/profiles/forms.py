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
        fields = ['avatar', 'bio']

class ForgotPWForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class createActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category','description','location','supervisors','participants','startDate', 'endDate']
        widget={
            'name': forms.TextInput(attrs={'class':'input'}),
            'category': forms.TextInput(attrs={'class':'input'}),
            'description': forms.TextInput(attrs={'class':'input'}),
            'location': forms.TextInput(attrs={'class':'input'}),
            'supervisors': forms.TextInput(attrs={'class':'input'}),
            'participants': forms.TextInput(attrs={'class':'input'}),

        }

