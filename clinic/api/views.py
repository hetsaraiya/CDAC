import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def registerpatient(request):
    if request.method == "POST":
        patient = Patient()
        patient.name = request.POST.get('name')
        patient.contact = request.POST.get('number')
        patient.email = request.POST.get('email')
        patient.password = request.POST.get('pass')


        patient.save()
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        contact = request.POST['mno']
        pass1 = request.POST['pass']

        user = Patient.objects.filter(email=username, contact=contact, password=pass1).first()
        
        if user:
            appointments = Appointment.objects.filter(patient_email=username, patient_contact=contact,)
            return render(request,'detail.html',{'appointments':appointments})
        else:
            return redirect('login')
        
def contact(request):
    if request.method == 'POST':
        username = request.POST['name']
        email=request.POST['email']
        subject10 = request.POST['subject']
        message10 = request.POST['message']

        subject = ' Conformation from Clinic'
        message = f'Thank you for submitting your details, {username}.\n\n'
        message += f'Client Name: {username}\n'
        message += f'Email: {email}\n'
        message += f'Subject: {subject10}\n'
        message += f'Message: {message10}\n\n'
        message += 'Our Expert will get back to you shortly.'

        from_email = settings.EMAIL_HOST_USER  # Replace with your email
        to_email = [email,]

        email_message = EmailMessage(subject, message, from_email, to_email)
        
        try:
            email_message.send()
        except Exception as e:
            print(f"Error sending email: {e}")
        return redirect('home')
            
    
def bookapp(request):
    if request.method == 'POST':
        appointment = Appointment()
        appointment.patient_name = request.POST.get('name')
        appointment.doctor_details = request.POST.get('doctor_name')
        appointment.patient_contact = request.POST.get('patient_contact')
        appointment.patient_email = request.POST.get('patient_email')
        appointment.appointment_date = request.POST.get('datebackend')
        appointment.appointment_time = request.POST.get('timebackend')
        appointment.description = request.POST.get('description')
        patient=Patient.objects.filter(email=appointment.patient_email,contact=appointment.patient_contact).first()
        if patient:
            appointment.patient_details = patient

        appointment.save()
        return redirect('appointment')

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
    
def register_doctor(request):
    if request.method == 'POST':
        doctor = Doctor()
        doctor.name = request.POST.get('name')
        doctor.speciality = request.POST.get('speciality')
        doctor.qualification = request.POST.get('qualification')
        doctor.profile = request.FILES.get('profile')
        doctor.address = request.POST.get('address')
        doctor.contact = request.POST.get('contact')
        doctor.email = request.POST.get('email')
        doctor.save()

def feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.title = request.POST.get('title')
        feedback.doctor = request.POST.get('doctor')
        feedback.gender = request.POST.get('gender')
        feedback.rate = request.POST.get('rate')
        feedback.comment = request.POST.get('comment')
        feedback.recieve = request.POST.get('recieve')
        feedback.contact = request.POST.get('contact')
        feedback.save()