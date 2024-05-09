from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).exists()
        if user:
            check_pass = User.objects.get(username=username)
            if check_password(password, check_pass.password):
                messages.success(request, 'Yor are login in !')
                return redirect('index')
            else:
                messages.error(request,'Wong Password !')
                return redirect('login')
        else:
            messages.error(request, 'Username dose bot existed !')
            return redirect('login')
    
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username existed !')        
                return render('register')
            else:
                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save()
                messages.error(request, 'You are registered !')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
