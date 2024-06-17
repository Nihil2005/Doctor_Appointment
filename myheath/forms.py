# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Doctor, Patient

class DoctorSignUpForm(UserCreationForm):
    doctor_name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
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
    specialty = forms.ChoiceField(choices=SPECIALTY_CHOICES)
    experience = forms.IntegerField()
    qualification = forms.CharField(max_length=255)
    working_hospital = forms.CharField(max_length=255)
    hospital_address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)
    doctor_certificate = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'doctor_name', 'age', 'gender', 'specialty', 'experience', 'qualification', 'working_hospital', 'hospital_address', 'phone', 'address', 'doctor_certificate']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            doctor = Doctor.objects.create(
                user=user,
                name=self.cleaned_data['doctor_name'],
                age=self.cleaned_data['age'],
                gender=self.cleaned_data['gender'],
                specialty=self.cleaned_data['specialty'],
                experience=self.cleaned_data['experience'],
                qualification=self.cleaned_data['qualification'],
                working_hospital=self.cleaned_data['working_hospital'],
                hospital_address=self.cleaned_data['hospital_address'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                doctor_certificate=self.cleaned_data['doctor_certificate']
            )
            doctor.save()
        return user


# forms.py

class PatientSignUpForm(UserCreationForm):
    patient_name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)
    medial_reports = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'patient_name', 'age', 'gender', 'phone', 'address', 'medial_reports']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            patient = Patient.objects.create(
                user=user,
                name=self.cleaned_data['patient_name'],
                age=self.cleaned_data['age'],
                gender=self.cleaned_data['gender'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                medial_reports=self.cleaned_data['medial_reports']
            )
            patient.save()
        return user
