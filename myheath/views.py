from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import DoctorSignUpForm, PatientSignUpForm

from django.contrib.auth import authenticate, login

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up as a doctor!')
            return redirect('doctor_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = DoctorSignUpForm()
    return render(request, 'auth/doctor_signup.html', {'form': form})
def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user object yet
            user.is_patient = True  # Set the user as a patient
            user.save()  # Save the user object
            form.save()  # Save the form data (patient profile)
            login(request, user)
            messages.success(request, 'You have successfully signed up as a patient!')
            return redirect('patient_dashboard')  # Redirect to patient dashboard
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PatientSignUpForm()
    return render(request, 'auth/patient_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_doctor:
                        return redirect('doctor_dashboard')
                    elif user.is_patient:
                        return redirect('patient_dashboard')
                else:
                    messages.error(request, 'Your account is inactive.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def doctor_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_doctor:
        return redirect('login')
    # Add logic to display doctor dashboard
    return render(request, 'doctor_dashboard.html')

def patient_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_patient:
        return redirect('login')
    # Add logic to display patient dashboard
    return render(request, 'dash/patient_dashboard.html')
