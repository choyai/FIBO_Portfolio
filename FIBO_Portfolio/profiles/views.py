from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'profiles/index.html')

def login(request):
    return render(request, 'profiles/login.html')

def forgotpassword(request, user_id):
    return render(request, 'profiles/profilepage.html')

def changepassword(request, user_id):
    return render(request, 'profiles/changepassword.html')


def profile(request, user_id):
    return render(request, 'profiles/profilepage.html')
def privacy(request, user_id):
    return render(request, 'profiles/privacy.html')

def personaledit(request, user_id):
    return render('profile/personaledit.html')
def academicedit(request, user_id):
    return render(request, 'profiles/academicedit.html')
def awardedit(request, user_id):
    return render(request, 'profiles/awardedit.html')
def workedit(request, user_id):
    return render(request, 'profiles/worknexperienceedit.html')



def academic(request, user_id):
    return render(request, 'profiles/academic.html')
def award(request, user_id):
    return render(request, 'profiles/award.html')
def work(request, user_id):
    return render(request, 'profiles/work.html')

def profilepage(request, user_id):
    return render(request, 'profiles/profilepage.html')


def organization(request):
    return render(request, 'profiles/organization.html')

def aboutus(request):
    return render(request, 'profiles/aboutus.html')

def edit(request):
    return HttpResponse('Edit page')
