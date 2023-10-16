from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from clientdata import models as cd
import requests
import hashlib
import hmac
import json
# Create your views here.


def POST_CMDB_VIEW(request):
    
    if request.method == 'POST':
        titulo = request.POST['txtTitulo']
        description = request.POST['txtFIELDDetail']
        status = request.POST['OptionStatus']
        client = request.POST['OptionClient']
        
        
        #Buscar las instancias de los modelos basados en nombre
        cliente = cd.Cliente.objects.get(nombre_empresa=client)
        estado = models.Status_Implementaciones.objects.get(nombre_status=status)
        
        implementacion = models.Implementaciones.objects.create(
            titulo = titulo,
            detalle = description,
            cliente = cliente,
            status_interno = estado
        
        )
        
        url = "https://napdelcaribe.n-c-s.net/json.pl/tickets/create"
        access_key = "a96e787f14e1504c94251801a6012939"
        secret = "935f058b88068e6368a707942268f93d"

        # Convertir la clave y el mensaje a formato de bytes
        access_key_bytes = access_key.encode('utf-8')
        secret_bytes = secret.encode('utf-8')
        url_bytes = url.encode('utf-8')

        # Generar firma HMAC-SHA1
        h = hmac.new(secret_bytes, url_bytes, hashlib.sha1)
        hmac_signature = h.hexdigest()

        # Encabezados de la solicitud
        headers = {
            "HMAC": hmac_signature,
            "KEY": access_key,
            "Content-Type": "application/json"
        }
        
        ticket_data = {
            "fields": {
                "status": {
                    "data": "1"
                },
                "title": {
                    "data": titulo
                },
                "details": {
                    "data": description
                },
                "priority": {
                    "data": "30"
                },
                "assigned_groups":{
                    "data":["14"]
                },
            }
        }
    
        # Convertir los datos del ticket a JSON
        ticket_json = json.dumps(ticket_data)

        # Realizar solicitud POST
        response = requests.post(url, data={"json": ticket_json}, headers=headers)
    
    return redirect('Implementaciones')


def Implementaciones_view(request):
    internal_status = models.Status_Implementaciones.objects.all()
    imp = models.Implementaciones.objects.all()
    ClientList = cd.Cliente.objects.all()
    
    context = {
        "status":internal_status,
        "implementaciones":imp,
        "clientes":ClientList
    }
    
    return render(request, 'pages/formularios/formularios_implementaciones.html', context)
