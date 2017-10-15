from django.shortcuts import render

def index(request):
    return render(request, 'activities/ActivityPage.html')

def createActivity(request):
    return render(request, 'activities/createActivity.html')

#def activity(request):
#    return render(request, 'activities/ActivityPage.html')
