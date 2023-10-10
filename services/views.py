from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.

@login_required
def Service_Order_View(request):
    order = models.Ordenes_De_Servicio.objects.all()
    service = models.servicios.objects.all()
    status = models.status.objects.all()
    
    return render(request, 'pages/client_control/service_order.html', {"order":order,
                                                                       "service":service,
                                                                       "status":status})


