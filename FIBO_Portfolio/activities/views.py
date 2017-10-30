from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

class ActivitiesIndex(generic.ListView):
    tmeplate_name = 'activities/ActivitiesPage.html'

    def get_queryset(self):
        return Activity.objects.all()

class ActivitiesDetail(generic.DetailView):
    model = Activity
    template_name = 'activities/ActivityPage.html'

class ActivitiesCreate(CreateView):
    model = Activity
    fields = ['name', 'category', 'description', 'location', 'supervision', 'location', 'supervisor', 'participants']

def create(request):
    return render(request, 'activities/createActivity.html')
def edit(request): # must include ID?
    return render(request, 'activities/editActivity.html')
def profile(request, user_id):
    return render(request, 'activity/myactivity.html')

def activity(request):
    return render(request, 'activities/activity.html')
def home(request):
    return render(request, 'activities/ActivitiesPage.html')

def myactivities(request, user_id):
    return render(request, 'activities/myactivity.html')
