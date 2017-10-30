from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import  BytesIO
from django.template import loader

def home(request):
    return render(request, 'profiles/index.html')

def profile(request, user_id):
    return render(request, 'profiles/profilepage.html')

def edit(request, user_id):
    return HttpResponse('This will be the profile edit page')

def academic(request, user_id):
    return render(request, 'profiles/academic.html')
def award(request, user_id):
    return render(request, 'profiles/award.html')
def changepassword(request, user_id):
    return render(request, 'profiles/changepassword.html')
def privacy(request, user_id):
    return render(request, 'profiles/privacy.html')
def profilepage(request, user_id):
    return render(request, 'profiles/profilepage.html')
def work(request, user_id):
    return render(request, 'profiles/work.html')
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