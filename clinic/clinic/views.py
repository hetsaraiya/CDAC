from django.shortcuts import render
from api.models import *
from api.views import *


def home(request):
    doctors_list=Doctor.objects.all()
    return render(request,'index.html',{'doctors': doctors_list})

def login(request):
    return render(request,'login.html')

def about(request):
    doctors_list=Doctor.objects.all()
    return render(request,'about.html',{'doctors': doctors_list})

def service(request):
    return render(request,'service.html')

def feature(request):
    return render(request,'feature.html')

def team(request):
    doctors_list=Doctor.objects.all()
    return render(request,'team.html', {'doctors': doctors_list})

def contact(request):
    doctors_list=Doctor.objects.all()
    return render(request,'contact.html',{'doctors': doctors_list})

def appointment(request):
    doctors_list=Doctor.objects.all()
    return render(request,'appointment.html',{'doctors': doctors_list})

def not_found(request):
    return render(request,'404.html')

def testimonial(request):
    return render(request,'testimonial.html')

def registeration(request):
    return render(request,'regi.html')

def detail(request):
    return render(request,'detail.html')

def newindex(request):
    return render(request,'newindex.html')

def base(request):
    return render(request,'base.html')

def doctor(request):
    return render(request,'doctor.html')

def payment(request):
    return render(request,'payment.html')

def feedback(request):
    return render(request,'feedback.html')

def admin(request):
    return render(request,'admin.html')