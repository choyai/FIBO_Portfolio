from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import  BytesIO
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import *


class UserFormView(View):
    form_class = UserForm
    template_name = 'profiles/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profiles:home')
        return render(request, self.template_name, {'form': form})


def home(request):
    return render(request, 'profiles/home.html')

def forgotpassword(request, user_id):
    return render(request, 'profiles/forgotpassword.html')

def changepassword(request, user_id):
    return render(request, 'profiles/changepassword.html')

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profiles/profilepage.html'

class AcademicView(generic.DetailView):
    model = Profile
    template_name = 'profiles/academic.html'

class AwardView(generic.DetailView):
    model = Profile
    template_name = 'profiles/award.html'

class WorkView(generic.DetailView):
    model = Profile
    template_name = 'profiles/work.html'

class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profiles/personaledit.html'
    fields = ['user', 'bio', 'birthDate', 'location', 'phone', 'emergencyPhone', 'congenitalDisease']

class ExecutiveTeamView(generic.DetailView):
    model = Profile
    template_name = 'prfiles/organization/executive_team.html'

class LecturerAndResearcher(generic.DetailView):
    model = Profile
    template_name = 'profiles/organization/lecturerandresearcher.html'

class AdjunctionLecturer(generic.DetailView):
    model = Profile
    template_name = 'profiles/organization/adjunct_lecturer.html'

class Engineer(generic.DetailView):
    model = Profile
    template_name = 'profiles/organization/engineer.html'

class Officer(generic.DetailView):
    module = Profile
    template_name = 'profiles/organization/officer.html'

class Student(generic.DetailView):
    module = Profile
    template_name = 'profiles/organization/#'


def privacy(request, user_id):
    return render(request, 'profiles/privacy.html')

def organization(request):
    return render(request, 'profiles/organization.html')

def aboutus(request):
    return render(request, 'profiles/aboutus.html')

def pdf_view(request):
    response = HttpResponse(content_type='profiles/application/pdf')
    response['Content-Disposition'] = 'attachment; filename ="somefilename.pdf"'

    buffer = BytesIO

    p = canvas.Canvas(response)

    p.drawString(100, 100, "My PDF")

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def edit(request):
    return HttpResponse('Edit page')
