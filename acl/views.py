from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from cosmos import models as cosmos
from clientdata import models as cd

# Create your views here.

@login_required
def Formularios_ACL(request):
    return render(request, 'pages/formularios/formularios_acl.html')


@login_required
def Permanente_Views(request):
    permanente = models.permanente.objects.all().order_by('-fecha_registro')
    permanente_cosmos = cosmos.Acl.objects.all().order_by('-fecha')
    categorias = models.categoria.objects.all()
    ClientList = cd.Cliente.objects.all()
    
    context = {
        'permanente':permanente,
        'cosmos':permanente_cosmos,
        'categorias':categorias,
        'clientes':ClientList
    }
    
    return render(request, 'admin_template/pages/landing/content/acl/permanente.html', context)

        
@login_required
def Restringido_Views(request):
    restringidos = cosmos.Restringidos.objects.all().order_by('-fecha')
    
    context = {
        'restringidos':restringidos 
    }
    
    return render(request, 'admin_template/pages/landing/content/acl/restringido.html', context)


@login_required
def Temporal_Views(request):
    temporal_cosmos = cosmos.AclTemporal.objects.all().order_by('-fecha_entrada')
    ClientList = cosmos.Empresas.objects.all()

    context = {
        'temporal_cosmos':temporal_cosmos,
        'clientes':ClientList
    }
    return render(request, 'admin_template/pages/landing/content/acl/temporal.html', context)
