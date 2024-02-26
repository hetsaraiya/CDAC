"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("service/",views.service,name="service"),
    path("404/",views.not_found,name="404"),
    path("feature/",views.feature,name="feature"),
    path("team/",views.team,name="team"),
    path("contact/",views.contact,name="contact"),
    path("appointment/",views.appointment,name="appointment"),
    path("testimonial/",views.testimonial,name="testimonial"),
    path("appointment/",views.appointment,name="appointment"),
    path("registration/",views.registeration,name="registeration"),
    path("login/",views.login,name="login"),
    path("detail/",views.detail,name="detail"),
    path("doctor/",views.doctor,name="doctor"),
    path("payment/",views.payment,name="payment"),
    path("feedback/",views.feedback,name="feedback"),
    path("admin-panel/",views.admin,name="admin"),
    path("admin-registration/",views.adminreg,name="admin-registration"),
    path("admin-feedback/",views.adminfeedback,name="admin-feedback"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
