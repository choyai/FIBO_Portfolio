from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'profiles/index.html')

def profile(request, user_id):
    return render(request, 'profiles/profilepage.html')

def edit(request, user_id):
    return HttpResponse('This will be the profile edit page')

def academic(request, user_id):
    return render(request, 'profiles/academic.html')
def award(request, user_id):
    return render(request, 'profiles/award.html')
def changepassword(request, user_id):
    return render(request, 'profiles/changepassword.html')
def privacy(request, user_id):
    return render(request, 'profiles/privacy.html')
def profilepage(request, user_id):
    return render(request, 'profiles/profilepage.html')
def work(request, user_id):
    return render(request, 'profiles/work.html')
def organization(request):
    return render(request, 'profiles/organization.html')

def aboutus(request):
    return render(request, 'profiles/aboutus.html')

