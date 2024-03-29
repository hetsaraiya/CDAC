from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.

class DoctorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','name', 'speciality', 'qualification', 'profile', 'address', 'contact', 'email')
    search_fields = ['id','name', 'speciality', 'qualification', 'profile', 'address', 'contact', 'email']

class PatientAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','name', 'contact', 'email', 'password')
    search_fields = ['id','name', 'contact', 'email', 'password']

class AppointmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','patient_details', 'patient_contact', 'patient_email', 'doctor_details')
    search_fields = ['id','patient_details', 'patient_contact', 'patient_email', 'doctor_details']

class ServicesAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','speciality_title', 'speciality_description')
    search_fields = ['id','speciality_title', 'speciality_description']     

class FeedbackAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','title', )
    search_fields = ['id','title', ]      

class PaymentsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','full_name', 'name_on_card', 'name_on_card', )
    search_fields = ['id','full_name', 'name_on_card', 'name_on_card', ]         

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Payments,PaymentsAdmin)