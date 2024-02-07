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
    patient_contact = PhoneNumberField(null=False, blank=False)
    patient_email = models.EmailField()
    doctor_details = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    appointment_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.patient_details.name