from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

def home(request):
    return render(request, 'profiles/index.html')

def profile(request, user_id):
    return render(request, 'profiles/profilepage.html')

def edit(request, user_id):
    return HttpResponse('This will be the profile edit page')
