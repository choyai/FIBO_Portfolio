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

# def changepassword(request, user_id):
#    return render(request, 'profiles/changepassword.html')

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profiles/profilepage.html'

class AcademicFormView(View):
    form_class = AcademicForm
    template_name = 'profiles/academicedit.html'

    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

class AcademicView(generic.DetailView):
    model = Profile
    template_name = 'profiles/academic.html'

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

def pdf_view(request):
    response = HttpResponse(content_type='profiles/application/pdf')
    response['Content-Disposition'] = 'attachment; filename ="somefilename.pdf"'

    buffer = BytesIO

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 20)
    p.drawString(330,740,"Name : ")
    p.setFont("Helvetica", 14)
    p.drawString(350,700,"age : ")
    p.drawString(350,680,"email : ")
    p.drawString(350,660,"phone : ")
    p.drawString(350,640,"address : ")

    p.setFont("Helvetica", 18)
    p.drawString(80,540,"Academic")
    p.line(80,530,250,530)
    p.drawString(80,390,"Work and experience")
    p.line(80,380,250,380)
    p.drawString(80,240,"Award")
    p.line(80,230,250,230)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def edit(request):
    return HttpResponse('Edit page')
