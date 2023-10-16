from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from clientdata import models as cd
from services import models as so
from acl import models as acl
from cosmos import models as cosmos

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Usuario autenticado correctamente")
            return redirect('Dashboard')  
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            print("Error de autenticación")

    return render(request, 'home.html')

def login_view2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Usuario autenticado correctamente")
            return redirect('Dashboard') 
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            print("Error de autenticación")

    return render(request, 'accounts/registration/login.html')

# 404 error template
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


def custom_page_server_error(request, exception):
    return render(request, '500.html', status=500)

@login_required

def Admin_Page_Service_Center(request):
    ServiceOrder = so.Ordenes_De_Servicio.objects.count()
    CountClient = cd.Cliente.objects.count()
    RestritedClient = cosmos.Restringidos.objects.count()
    
    if request.user.is_authenticated:
        nombre = request.user.first_name
        apellido = request.user.last_name
        nombre_usuario = nombre+(' ')+apellido
        
        
    context = {
        'Clients': CountClient,
        'ServiceOrder': ServiceOrder,
        'restringidos': RestritedClient,
        'nombre_usuario': nombre_usuario
    }

    return render(request, 'admin_template/index.html', context)



def logout_view(request):
    logout(request)
    return redirect('Home')
