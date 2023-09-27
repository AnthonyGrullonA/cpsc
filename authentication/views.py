from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')  
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')

    return render(request, 'accounts/registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('Home')