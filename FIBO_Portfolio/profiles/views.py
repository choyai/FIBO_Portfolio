from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, DetailView
from .forms import *
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import *

class GPAUpdateView(UpdateView):
    model = Grade
    template_name = 'profiles/academicedit.html'
    fields = 'GPA'

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

class PrivacyEditView(FormView):
    form_class = PrivacyForm
    template_name = 'profiles/privacy.html'
    success_url = reverse_lazy('profiles:home')

def home(request):
    return render(request, 'profiles/home.html')

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profiles/profilepage.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['ability_set'] = self.get_object().ability_set.all()
        context['image_set'] = self.get_object().user.userimage_set.all()
        return context


class AcademicFormView(UpdateView):
    model = Profile
    template_name = 'profiles/academicedit.html'
    fields = ['admission', 'scholarship']

class GradeCreateView(CreateView):
    model = Grade
    template_name = 'profiles/gradeEdit.html'
    fields = ['profile', 'semester', 'creditTotal', 'GPA']


class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'profiles/gradeEdit.html'
    fields = ['GPA']

class AcademicView(generic.DetailView):
    model = Profile
    template_name = 'profiles/academic.html'

    def get_context_data(self, **kwargs):
        context = super(AcademicView, self).get_context_data(**kwargs)
        context['grade_set'] = self.get_object().grade_set.all()
        context['edu_set'] = self.get_object().educationbackground_set.all()
        return context



class EducationalBackground(CreateView):
    model = EducationBackground
    template_name = 'profiles/educationalBackground.html'
    fields = ['profile', 'degree', 'major', 'school']


class AwardView(generic.DetailView):
    model = Profile
    template_name = 'profiles/award.html'

class AwardFormView(View):
    form_class = createActivityForm
    template_name = 'profiles/awardedit.html'
    def get(self, request, pk):
        return render(request, self.template_name)

class WorkView(generic.DetailView):
    model = Profile
    template_name = 'profiles/work.html'

class WorkFormView(View):
    form_class = createActivityForm
    template_name = 'profiles/worknexperienceedit.html'
    def get(self, request,pk):
        return render(request, self.template_name)

class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profiles/profiles_form.html'
    fields = ['user', 'avatar', 'bio', 'birthDate', 'location', 'phone', 'emergencyPhone', 'congenitalDisease']

class AwardEdit(generic.DetailView):
    model = Profile
    template_name = 'profiles/awardedit.html'

class ExecutiveTeamView(View):
    template_name = 'profiles/executive_team.html'
    def get(self, request):
        return render(request, self.template_name)

class LecturerAndResearcherView(View):
    template_name = 'profiles/lecturerandresearcher.html'
    def get(self, request):
        return render(request, self.template_name)

class AdjunctionLecturerView(View):
    template_name = 'profiles/adjunct_lecturer.html'
    def get(self, request):
        return render(request, self.template_name)

class EngineersView(View):
    template_name = 'profiles/engineer.html'
    def get(self, request):
        return render(request, self.template_name)

class OfficerView(View):
    template_name = 'profiles/officer.html'
    def get(self, request):
        return render(request, self.template_name)

class StudentView(generic.DetailView):
    template_name = 'profiles/#'
    def get(self, request):
        return render(request, self.template_name)

def organization(request):
    return render(request, 'profiles/organization.html')

def aboutus(request):
    return render(request, 'profiles/aboutus.html')


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def pdf_view(request):
    profile = request.user.user
    response = HttpResponse(content_type='profiles/application/pdf')
    response['Content-Disposition'] = 'attachment; filename ="resume.pdf"'

    #buffer = BytesIO

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 20)
    p.drawString(330,740, "Name : " + request.user.first_name + " " + request.user.last_name)
    p.setFont("Helvetica", 14)
    p.drawString(350,700,"age : " + str(calculate_age(profile.birthDate)))
    p.drawString(350,680,"email : " + request.user.email)
    p.drawString(350,660,"phone : " + profile.phone )
    p.drawString(350,640,"address : " + profile.location)

    p.setFont("Helvetica", 18)
    p.drawString(80,540,"Academic")
    p.line(80,530,250,530)
    p.drawString(80,390,"Work and experience")
    p.line(80,380,250,380)
    p.drawString(80,240,"Award")
    p.line(80,230,250,230)
    p.showPage()
    p.save()

    #pdf = buffer.getvalue()
    #buffer.close()
    response.write(p)
    return response

def edit(request):
    return HttpResponse('Edit page')
