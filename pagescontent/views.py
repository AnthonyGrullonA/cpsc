from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.

def home(request):
    return render(request, 'home.html')

#Prueba de plantillas AdminLTE (Despues cambiar nombre de funciones)
def adminlte(request):
    return render(request, ('admin_template/index.html'))

def adminvacio(request):
    return render(request, 'admin_template/starter.html')