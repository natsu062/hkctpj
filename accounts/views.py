from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
#from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
                messages.error(request,'Wong Password !')
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
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
