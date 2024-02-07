import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers

# Create your views here.

def registerpatient(request):
    if request.method == "POST":
        patient = Patient()
        patient.name = request.POST.get('name')
        patient.contact = request.POST.get('number')
        patient.email = request.POST.get('email')
        patient.password = request.POST.get('pass')
        patient.save()

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(name=username, password=pass1)

        return HttpResponse(json.dumps({"msg": " login successfull "}),content_type="application/json",)
    
def bookapp(request):
    if request.method == 'POST':
        appointment = Appointment
        appointment.patient_details = request.POST.get('patient_details')
        appointment.doctor_details = request.POST.get('doctor_name')
        appointment.patient_contact = request.POST.get('patient_contact')
        appointment.patient_email = request.POST.get('patient_email')
        appointment.appointment_date = request.POST.get('date')
        appointment.appointment_time = request.POST.get('time')
        appointment.description = request.POST.get('description')
        appointment.save()

def doctors_list(request):
    if request.method == 'GET':
        doc_list = Doctor.objects.all()
        data = serializers.serialize("json", doc_list)
        return HttpResponse(data, content_type="application/json")
    
def services_list(request):
    if request.method == 'GET':
        ser_list = Services.objects.all()
        data = serializers.serialize("json", ser_list)
        return HttpResponse(data, content_type="application/json")