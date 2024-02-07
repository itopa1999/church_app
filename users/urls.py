from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    
    path('register_form', views.register_form, name="register_form"),
    path('attendance', views.attendance, name="attendance"),
    
]