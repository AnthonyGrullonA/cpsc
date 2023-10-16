from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from clientdata import models as cd
# Create your views here.

@login_required
def Service_Order_View(request):
    order = models.Ordenes_De_Servicio.objects.all()
    service = models.servicios.objects.all()
    status = models.status.objects.all()
    ClientList = cd.Cliente.objects.all()

    return render(request, 'pages/client_control/service_order.html', {"order":order,
                                                                       "service":service,
                                                                       "status":status,
                                                                       "clientes":ClientList})


def ServiceOrderRegisterView(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['OptionCliente']
        nombre_servicio = request.POST['OptionService']
        nombre_status = request.POST['OptionStatus']
        
        #Buscando en instancias basadas en nombres de modelos
        cliente = cd.Cliente.objects.get(nombre_empresa=nombre_cliente)
        servicio = models.servicios.objects.get(nombre_servicio=nombre_servicio)
        status = models.status.objects.get(estado_status=nombre_status)
        
        ServiceOrder = models.Ordenes_De_Servicio.objects.create(
            clientes = cliente,
            servicio_contratado = servicio,
            status = status
        )
    
    return redirect('ServiceOrder')


@login_required
def EliminarOrdenView(request, id_ods):
    order = get_object_or_404(models.Ordenes_De_Servicio, id_ods=id_ods)
    order.delete()
    return redirect('ServiceOrder')

