from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')