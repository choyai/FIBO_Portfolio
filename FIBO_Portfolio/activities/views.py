from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'activities/createActivity.html')

def home(request):
    return render(request, 'activities/ActivitiesPage.html')

def activity(request):
    return render(request, 'activities/activity.html')
