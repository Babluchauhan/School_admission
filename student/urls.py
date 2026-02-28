from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('admission_form', views.admission_form, name='admission_form'),
]