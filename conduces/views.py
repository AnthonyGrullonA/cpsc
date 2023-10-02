from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Input_Conduce_View(request):
    return render(request, 'pages/conduces/entrada.html')

@login_required
def Output_Conduce_View(request):
    return render(request, 'pages/conduces/salida.html')