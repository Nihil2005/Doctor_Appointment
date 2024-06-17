# models.py

from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')  # Specify unique related_name
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions') 

    class Meta:
        db_table = 'custom_user'


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    SPECIALTY_CHOICES = (
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Urologist', 'Urologist'),
        ('Oncologist', 'Oncologist'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Endocrinologist', 'Endocrinologist'),
        ('Rheumatologist', 'Rheumatologist'),
        ('Otolaryngologist', 'Otolaryngologist'),
        ('Hematologist', 'Hematologist'),
        ('Pulmonologist', 'Pulmonologist'),
        ('Nephrologist', 'Nephrologist'),
        ('Plastic Surgeon', 'Plastic Surgeon'),
        ('Orthopedic Surgeon', 'Orthopedic Surgeon'),
        ('ENT Surgeon', 'ENT Surgeon'),
        ('Vascular Surgeon', 'Vascular Surgeon'),
        ('Neurosurgeon', 'Neurosurgeon'),
        ('Dentist', 'Dentist'),
        ('Gynaecologist', 'Gynaecologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Oncologist', 'Oncologist'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Endocrinologist', 'Endocrinologist'),
        ('Rheumatologist', 'Rheumatologist'),
        ('Otolaryngologist', 'Otolaryngologist'),
        ('Hematologist', 'Hematologist'),
        ('Pulmonologist', 'Pulmonologist'),
        ('Nephrologist', 'Nephrologist')
    )
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES)
    experience = models.PositiveIntegerField()
    qualification = models.CharField(max_length=255)
    working_hospital = models.CharField(max_length=255)
    hospital_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    doctor_certificate = models.FileField(upload_to='doctor_certificate/', null=True, blank=True)
  
    # Add additional fields for doctor profile





class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    medial_reports = models.FileField(upload_to='medial_reports/', null=True, blank=True)
    
    # Add additional fields for patient profile
  
