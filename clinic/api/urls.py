from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("register/", views.registerpatient, name="registerpatient"),
    path("login/", views.login, name="login"),
    path("bookapp/", views.bookapp, name="bookapp"),
    path("doctorslist/", views.doctors_list, name="doctors_list"),
    path("serviceslist/", views.services_list, name="services_list"),
]