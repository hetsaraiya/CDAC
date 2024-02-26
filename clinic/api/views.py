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
        doctor.name = request.POST.get('name')+" "+request.POST.get('last_name')
        doctor.speciality = request.POST.get('speciality')
        doctor.qualification = request.POST.get('qualification')
        doctor.profile = request.FILES.get('profile')
        doctor.address = request.POST.get('city')+" "+request.POST.get('country')
        doctor.contact = request.POST.get('contact')
        doctor.email = request.POST.get('email')
        doctor.profile = request.FILES.get('image')
        doctor.save()
        return redirect('team')

def feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.title = request.POST.get('name')
        doctor= request.POST.get('doctor_name')
        feedback.gender = request.POST.get('gender')
        feedback.rate = request.POST.get('rate')
        feedback.comment = request.POST.get('comments')
        feedback.recieve = True
        feedback.rate=request.POST.get('rating')
        #feedback.contact = request.POST.get('contact')
        feedback.doctor = Doctor.objects.get(id=doctor)

        feedback.save()
        return redirect('home')
    
def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        repass1= request.POST.get('number')
        

        if pass1 !=repass1:
            return HttpResponse("password not match go back and re write password")

        user = Patient.objects.filter(email=email).first()

        if user:
            user.password=pass1
            user.save()
            return redirect('login')
        else:
            return HttpResponse("User not found go back and regiter your self again with new credentials")    
        
def adminforgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        repass1= request.POST.get('number')
        

        if pass1 !=repass1:
            return HttpResponse("password not match go back and re write password")

        user = Patient.objects.filter(email=email).first()

        if user:
            user.password=pass1
            user.save()
            return redirect('admin')
        else:
            return HttpResponse("User not found go back and regiter your self again with new credentials")            
        

def payment(request):
    if request.method == 'POST':
        payment = Payments()
        payment.full_name = request.POST.get('name')
        payment.email = request.POST.get('email')
        payment.address = request.POST.get('address')
        payment.city = request.POST.get('city')
        payment.name_on_card = request.POST.get('cardName')
        payment.credit_card_number = request.POST.get('cardNum')
        payment.exp_month = request.POST.get('exp_month')
        payment.state = request.POST.get('state')
        payment.zip_code = request.POST.get('zip')
        payment.exp_year = request.POST.get('exp_year')
        payment.cvv = request.POST.get('cvv')

        print(payment.cvv)
        print("done pay")

        payment.save()
        return render(request, 'payment.html')
    else:
        return render(request, 'payment.html')