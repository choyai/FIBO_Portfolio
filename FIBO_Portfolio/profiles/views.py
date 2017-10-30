from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import  BytesIO
from django.template import loader
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'profiles/index.html')

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
                    return redirect('profiles:organization')
        return render(request, self.template_name, {'form': form})

def login1(request):
    return render(request, 'profiles/login.html')

def forgotpassword(request, user_id):
    return render(request, 'profiles/forgotpassword.html')

def changepassword(request, user_id):
    return render(request, 'profiles/changepassword.html')


def profile(request, user_id):
    return render(request, 'profiles/profilepage.html')
def privacy(request, user_id):
    return render(request, 'profiles/privacy.html')

def personaledit(request, user_id):
    return render('profile/personaledit.html')
def academicedit(request, user_id):
    return render(request, 'profiles/academicedit.html')
def awardedit(request, user_id):
    return render(request, 'profiles/awardedit.html')
def workedit(request, user_id):
    return render(request, 'profiles/worknexperienceedit.html')



def academic(request, user_id):
    return render(request, 'profiles/academic.html')
def award(request, user_id):
    return render(request, 'profiles/award.html')
def work(request, user_id):
    return render(request, 'profiles/work.html')

def profilepage(request, user_id):
    return render(request, 'profiles/profilepage.html')


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
