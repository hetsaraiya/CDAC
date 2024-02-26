import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Services(models.Model):
    speciality_title = models.CharField(max_length=20)
    speciality_description = models.TextField()

    def __str__(self):
        return self.speciality_title


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    speciality = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    qualification = models.CharField(max_length=30)
    profile = models.ImageField(upload_to="profile/")
    address = models.TextField()
    contact = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    contact = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient_details = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    patient_name= models.CharField(max_length=50, null=True, blank=True)
    
    patient_contact = PhoneNumberField(null=False, blank=False)
    patient_email = models.EmailField()
    doctor_details = models.CharField(max_length=30)
    appointment_date = models.CharField(max_length=10)
    appointment_time = models.CharField(max_length=10)
    description = models.TextField()
    time=models.TimeField(auto_now=True)

    def __str__(self):
        return self.patient_email

class Feedback(models.Model):
   
    title  = models.CharField(max_length=30, default="")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now)
    gender = models.CharField(max_length=20, default="")
    rate = models.CharField(max_length=20, default="")
    comment = models.TextField()
    recieve = models.BooleanField(default=False)
    contact = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Payments(models.Model):
    full_name = models.CharField(max_length=30, default="")
    email = models.EmailField()
    address = models.TextField(default="")
    city = models.CharField(max_length=10, default="")
    name_on_card = models.CharField(max_length=30,default="")
    credit_card_number = models.IntegerField()
    exp_month = models.CharField(max_length=10, default="")
    state = models.CharField(max_length=30, default="")
    zip_code = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.full_name