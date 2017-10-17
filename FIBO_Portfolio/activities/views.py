from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'activities/createActivity.html')

def activities_home(request):
    return render(request, 'activities/ActivitiesPage.html')
