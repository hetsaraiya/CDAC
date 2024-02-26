from django.contrib import admin
from django.urls import include, path
from . import views
app_name = "api"

urlpatterns = [
    path("registerpatient/", views.registerpatient, name="registerpatient"),
    path("login/", views.login, name="login"),
    path("bookapp/", views.bookapp, name="bookapp"),
    path("doctorslist/", views.doctors_list, name="doctors_list"),
    path("serviceslist/", views.services_list, name="services_list"),
    path("contact/", views.contact, name="contact"),
    path("register_doctor/", views.register_doctor, name="register_doctor"),
    path("feedback/", views.feedback, name="feedback"),
]