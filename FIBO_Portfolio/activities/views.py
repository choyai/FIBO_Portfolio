from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.views.generic import View, DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View
from django.shortcuts import render, redirect

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
    #    for person in form.cleaned_data['supervisors']:
    #        supervision = Supervision(activity=self.object, supervisor = person)
        self.object.save()
        for person in form.cleaned_data['participants']:
            participation = Participation(activity=self.object, participant=person)
            participation.save()
        return super(ModelFormMixin, self).form_valid(form)

class ActivitiesUpdate(UpdateView):
    model = Activity
    template_name = 'activities/activities_form.html'
    fields = ['name', 'category', 'description', 'location', 'location', 'supervisors', 'participants',
              'startDate', 'endDate']
    def form_valid(self, form):
        self.object = form.save(commit=False)
    #    for person in form.cleaned_data['supervisors']:
    #        supervision = Supervision(activity=self.object, supervisor = person)
        for person in form.cleaned_data['participants']:
            participation = Participation(activity=self.object, participant=person)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class MyActivitiesView(View):

    def get(self, request, pk):
        template_name = 'activities/myactivity.html'
        profile = Profile.objects.get(id = request.user.pk)
        queryset = profile.participation_set.all()
        context = {"verified_list": None, "unverified_list": None,}
        context["verified_list"] = queryset.filter(isVerified=True)
        context["unverified_list"] = queryset.filter(isVerified=False)

        return render(request, template_name, context)


class ActivitiesDelete(DeleteView):
    model = Activity
    template_name = 'activities/delete.html'
    success_url = reverse_lazy('activities:home')

class VerifyView(View):

    def get(self, request, pk):
        template_name = 'activities/verify.html'
        profile = Profile.objects.get(id = request.user.pk)
        queryset = profile.supervisor.all()
        context = {"verified_list": None, "unverified_list": None,}
        context["verified_list"] = queryset.filter(isVerified=True)
        context["unverified_list"] = queryset.filter(isVerified=False)

        return render(request, template_name, context)

def profile(request, user_id):
    return render(request, 'activity/myactivity.html')

def activity(request, activity_id):
    return render(request, 'activities/ActivityPage.html')

def home(request):
    return render(request, 'activities/ActivitiesPage.html')
