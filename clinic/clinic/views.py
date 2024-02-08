from django.shortcuts import render
from api.models import *
from api.views import *


def home(request):

    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def feature(request):
    return render(request,'feature.html')

def team(request):
    doctors_list=Doctor.objects.all()
    return render(request,'team.html', {'doctors': doctors_list})

def contact(request):
    return render(request,'contact.html')

def appointment(request):
    return render(request,'appointment.html')

def not_found(request):
    return render(request,'404.html')

def testimonial(request):
    return render(request,'testimonial.html')

def registeration(request):
    return render(request,'regi.html')