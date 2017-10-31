from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.core.urlresolvers import reverse_lazy

class ActivitiesIndex(generic.ListView):
    template_name = 'activities/index.html'

    def get_queryset(self):
        return Activity.objects.all()

class ActivitiesDetail(generic.DetailView):
    model = Activity
    template_name = 'activities/ActivityPage.html'

class ActivitiesCreate(CreateView):
    model = Activity
    template_name = 'activities/activities_form.html'
    fields = ['name', 'category', 'description', 'location', 'location', 'supervisors', 'participants',
              'startDate', 'endDate']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        for person in form.cleaned_data['supervisors']:
            supervision = Supervision(activity=self.object, supervisor = person)
        for person in form.cleaned_data['participants']:
            participation = Participation(activity=self.object, participant=person)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class ActivitiesUpdate(UpdateView):
    model = Activity
    template_name = 'activities/activities_form.html'
    fields = ['name', 'category', 'description', 'location', 'location', 'supervisors', 'participants',
              'startDate', 'endDate']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        for person in form.cleaned_data['supervisors']:
            supervision = Supervision(activity=self.object, supervisor = person)
        for person in form.cleaned_data['participants']:
            participation = Participation(activity=self.object, participant=person)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class ActivitiesDelete(DeleteView):
    model = Activity
    template_name = 'activities/delete.html'
    success_url = reverse_lazy('activities:home')

def profile(request, user_id):
    return render(request, 'activity/myactivity.html')

def activity(request, activity_id):
    return render(request, 'activities/ActivityPage.html')

def home(request):
    return render(request, 'activities/ActivitiesPage.html')

def myactivities(request, user_id):
    return render(request, 'activities/myactivity.html')
