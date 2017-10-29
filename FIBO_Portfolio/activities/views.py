from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def create(request):
    return render(request, 'activities/createActivity.html')
def activity(request):
    return render(request, 'activities/activity.html')
def home(request):
    return render(request, 'activities/ActivitiesPage.html')
