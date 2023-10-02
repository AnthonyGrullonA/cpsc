
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from datetime import datetime

@login_required
def Client_Contact_View(request):
    return render(request, 'pages/client_control/client_contact.html')


@login_required
def Client_List_View(request):
    ClientList = models.Cliente.objects.all()
    Entidad = models.Entidad.objects.all()
    Status = models.Status.objects.all()
    Operation = models.Operacion.objects.all()
    Industry = models.Industria.objects.all()
    Site = models.Localidad.objects.all()
    
    return render(request, 'pages/client_control/client_list.html', {"clientes":ClientList,
                                                                     "entidad":Entidad,
                                                                     "estado":Status,
                                                                     "operation":Operation,
                                                                     "industria":Industry,
                                                                     "site":Site})
@login_required
def RegistrarClientes(request):
    if request.method == 'POST':
        nombre_empresa = request.POST['txtNombreC']
        status_cliente_nombre = request.POST['OptionStatus']
        fecha_inicio_contrato_str = request.POST['DateField']
        rnc = request.POST['txtRNC']
        direccion = request.POST['txtFIELDDirection']
        tipo_operacion_nombre = request.POST['OptionOperation']
        tipo_entidad_nombre = request.POST['OptionSector']
        industria_nombre = request.POST['OptionIndustry']
        site_loc = request.POST['OptionSite']

        # Formatear la fecha en el formato correcto (YYYY-MM-DD)
        try:
            fecha_inicio_contrato = datetime.strptime(fecha_inicio_contrato_str, '%Y-%m-%d')
        except ValueError:
            # Manejar el error si la fecha no tiene el formato esperado
            fecha_inicio_contrato = None

        # Buscar la instancia de Status, Operacion, Entidad, Industria y Localidad
        status_cliente = models.Status.objects.get(status=status_cliente_nombre)
        tipo_operacion = models.Operacion.objects.get(operacion=tipo_operacion_nombre)
        tipo_entidad = models.Entidad.objects.get(entidad=tipo_entidad_nombre)
        industria = models.Industria.objects.get(nombre_industria=industria_nombre)
        site = models.Localidad.objects.get(localidad=site_loc)

        # Crear el cliente con las instancias correctas
        cliente = models.Cliente.objects.create(nombre_empresa=nombre_empresa,
                                               status_cliente=status_cliente,
                                               fecha_inicio_contrato=fecha_inicio_contrato,
                                               rnc=rnc,
                                               direccion=direccion,
                                               tipo_operacion=tipo_operacion,
                                               tipo_entidad=tipo_entidad,
                                               industria=industria,
                                               site=site)

        return redirect('/ClientList/')

