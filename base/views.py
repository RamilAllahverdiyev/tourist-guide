from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')


def register_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
        
        except:
            error_message = 'An error occurred during registration. Please try again.'
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
       
    return render(request, 'login.html')


def profile_page(request):
    return render(request, 'profile.html')
