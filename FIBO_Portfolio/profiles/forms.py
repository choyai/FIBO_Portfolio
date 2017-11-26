from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['semester', 'creditTotal', 'GPA']
        widget = {
            'semester': forms.NumberInput(attrs={'class':'input'}),
            'creditTotal': forms.NumberInput(attrs={'class':'input'}),
            'GPA': forms.NumberInput(attrs={'class':'input'})
        }

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

class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['friendViewPersonalInfo',
        'publicViewPersonalInfo',
        'friendViewAcademicInfo',
        'publicViewAcademicInfo',
        'friendViewExpInfo',
        'publicViewExpInfo'
        ]
        widget ={
            'friendViewPersonalInfo': forms.CheckboxInput(),
            'publicViewPersonalInfo': forms.CheckboxInput(),
            'friendViewAcademicInfo': forms.CheckboxInput(),
            'publicViewAcademicInfo': forms.CheckboxInput(),
            'friendViewExpInfo': forms.CheckboxInput(),
            'publicViewExpInfo': forms.CheckboxInput(),
        }

class createActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category', 'description', 'location', 'supervisors', 'participants', 'startDate', 'endDate']
        widget = {
            'name': forms.TextInput(attrs={'class':'input'}),
            'category': forms.TextInput(attrs={'class':'input'}),
            'description': forms.TextInput(attrs={'class':'input'}),
            'location': forms.TextInput(attrs={'class':'input'}),
            'supervisors': forms.TextInput(attrs={'class':'input'}),
            'participants': forms.TextInput(attrs={'class':'input'}),
<<<<<<< HEAD

        }
=======
        }
>>>>>>> master
