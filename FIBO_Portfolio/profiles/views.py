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
    def get_context_data(self, **kwargs):
        context = super(AwardView, self).get_context_data(**kwargs)
        context['award_set'] = self.get_object().participation_set.filter(activity__category__contains='award', isVerified=True)
        return context

class AwardFormView(View):
    form_class = createActivityForm
    template_name = 'profiles/awardedit.html'
    def get(self, request, pk):
        return render(request, self.template_name)

class WorkView(generic.DetailView):
    model = Profile
    template_name = 'profiles/work.html'
    def get_context_data(self, **kwargs):
        context = super(WorkView, self).get_context_data(**kwargs)
        context['class_pj_set'] = self.get_object().participation_set.filter(activity__category__contains='project', isVerified=True)
        context['lab_set'] = self.get_object().participation_set.filter(activity__category__contains="lab", isVerified=True)
        context['ta_set'] = self.get_object().participation_set.filter(activity__category__contains="teach", isVerified=True)
        context['competition_set'] = self.get_object().participation_set.filter(activity__category__contains="competition", isVerified=True)
        context['internship_set'] = self.get_object().participation_set.filter(activity__category__contains="internship", isVerified=True)
        return context


class WorkFormView(View):
    form_class = createActivityForm
    template_name = 'profiles/worknexperienceedit.html'
    def get(self, request,pk):
        return render(request, self.template_name)

class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profiles/profiles_form.html'
    fields = ['user', 'avatar','banner', 'bio', 'birthDate', 'location', 'phone', 'emergencyPhone', 'congenitalDisease']

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
    participationlist = profile.participation_set.filter(isVerified=True)
    awardlist = participationlist.filter(activity__category__contains='award')
    worklist = participationlist.filter(activity__category__contains='work')
    abilist = profile.ability_set.all()
    gradelist = profile.grade_set.all()
    #buffer = BytesIO

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 20)
    #p.drawString(20,760, "Resume" )
    p.drawString(25,790,  request.user.first_name + " " + request.user.last_name)
    p.setFont("Helvetica", 14)
    p.drawString(27,770,  "Institute of Field Robotics (FIBO)")
    p.line(25,763,750,761)

    p.setFont("Helvetica", 11)
    p.drawString(330,800,"EMAIL    " + request.user.email)
    p.drawString(330,785,"PHONE  " + profile.phone )
    p.setFont("Helvetica", 9)
    p.drawString(330,772,"Location     " + profile.location)

    p.setFont("Helvetica", 18)
    gpax = 0
    totalgrade = 0
    totalCredit = 0
    semes = 0
    for grade in gradelist:
        totalgrade += grade.GPA * grade.creditTotal
        totalCredit += grade.creditTotal
        semes += 1
    gpax = (totalgrade/totalCredit)
    format(gpax, '.2f')


    p.drawString(27,740,"Academic")
    p.line(27,738,110,738)
    p.setFont("Helvetica", 12)
    p.drawString(30,725, "GPAX of "+ str(semes) + " semester "+str(gpax))
    semes = 1
    yposleft = 712;
    for grade in gradelist:
        p.drawString(30,yposleft, "GPA of semester "+ str(semes)+ " : " +str(format(grade.GPA, '.2f')) + "  Credit : " + str(grade.creditTotal) )
        semes += 1
        yposleft -= 14;


    p.setFont("Helvetica", 18)
    yposleft -= 10;
    p.drawString(27,yposleft,"Work and Experience")
    yposleft -= 2;
    p.line(27,yposleft,200,yposleft)
    p.setFont("Helvetica", 12)
    yposleft -= 15;
    i = 1
    for work in worklist:
        p.drawString(30,yposleft, str(i)+ ". " + work.activity.name + "   Start : " +  str(work.activity.startDate) +  "  End: " + str(work.activity.endDate))
        yposleft -= 14;
        i +=1



    p.setFont("Helvetica", 18)
    yposleft -= 10;
    p.drawString(27,yposleft,"Awards")
    yposleft -= 2;
    p.line(27,yposleft,80,yposleft)
    p.setFont("Helvetica", 12)
    yposleft -= 15;
    for award in awardlist:
        p.drawString(30,yposleft,  " - " + award.activity.name + "   Date : " +  str(award.activity.startDate) )
        yposleft -= 14;



    p.setFont("Helvetica", 18)
    yposleft -= 10;
    p.drawString(27,yposleft,"Ablities")
    yposleft -= 2;
    p.line(27,yposleft,80,yposleft)
    p.setFont("Helvetica", 12)
    yposleft -= 15;
    for abi in abilist:
        p.drawString(30,yposleft,  " - " + abi.name )
        yposleft -= 14;


    p.line(0,50,1000,50)
    p.drawString(10,20,"FIBO Portfoilio FIBO Portfoilio FIBO Portfoilio FIBO Portfoilio FIBO Portfoilio FIBO Portfoilio FIBO Portfoilio ")

    p.showPage()
    p.save()

    #pdf = buffer.getvalue()
    #buffer.close()
    response.write(p)
    return response

def edit(request):
    return HttpResponse('Edit page')
