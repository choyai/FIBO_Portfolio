from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from django.template import loader

# Create your views here.

def create(request):
    return render(request, 'activities/createActivity.html')

<<<<<<< Updated upstream
def activities_home(request):
    return render(request, 'activities/ActivitiesPage.html')
=======
def home(request):
    return render(request, 'activities/index.html')

def activity(request):
    return render(request, 'activities/activity.html')
>>>>>>> Stashed changes
