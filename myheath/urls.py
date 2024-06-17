from django.urls import path
from . import views

urlpatterns = [
    path('doctor/signup/', views.doctor_signup, name='doctor_signup'),
    path('patient/signup/', views.patient_signup, name='patient_signup'),
    path('login/', views.user_login, name='login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
]
