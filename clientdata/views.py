from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from datetime import datetime
from django.http import JsonResponse


@login_required
def Client_Contact_View(request):
    
    contacto = models.Contacto.objects.all()
    ClientList = models.Cliente.objects.all()

    return render(request, 'pages/client_control/client_contact.html', {"contacto":contacto,
                                                                        "clientes": ClientList,})


@login_required
def Client_List_View(request):
    ClientList = models.Cliente.objects.all()
    Entidad = models.Entidad.objects.all()
    Status = models.Status.objects.all()
    Operation = models.Operacion.objects.all()
    Industry = models.Industria.objects.all()
    Site = models.Localidad.objects.all()

    return render(request, 'pages/client_control/client_list.html', {"clientes": ClientList,
                                                                    "entidad": Entidad,
                                                                    "estado": Status,
                                                                    "operation": Operation,
                                                                    "industria": Industry,
                                                                    "site": Site})



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
        cliente = models.Cliente.objects.create(
            nombre_empresa=nombre_empresa,
            status_cliente=status_cliente,
            fecha_inicio_contrato=fecha_inicio_contrato,
            rnc=rnc,
            direccion=direccion,
            tipo_operacion=tipo_operacion,
            tipo_entidad=tipo_entidad,
            industria=industria,
            site=site
        )

    # Después de procesar la creación o edición, redireccionar a la página de lista de clientes
    return redirect('ClientList')

@login_required
def RegistrarContactos(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        nombre_empresa = request.POST['OptionCliente']  # Usamos nombre_empresa en lugar de empresa
        identificacion = request.POST['txtIdentificacion']
        correo = request.POST['txtCorreo']
        telefono = request.POST['txtTelefono']
        cargo = request.POST['txtCargo']

        # Buscar la instancia de Cliente basada en el nombre de la empresa
        cliente = models.Cliente.objects.get(nombre_empresa=nombre_empresa)

        # Crear el contacto con las instancias correctas
        contacto = models.Contacto.objects.create(
            nombre_contacto=nombre,
            apellido_contacto=apellido,
            identificacion=identificacion,
            empresa=cliente,
            correo=correo,
            telefono=telefono,
            cargo=cargo
        )

    return redirect('ClientContact')


@login_required
def EliminarCliente(request, id_cliente):
    cliente = get_object_or_404(models.Cliente, id_cliente=id_cliente)
    cliente.delete()
    return redirect('ClientList')


@login_required
def EliminarContacto(request, id_contacto):
    contacto = get_object_or_404(models.Contacto, id_contacto=id_contacto)
    contacto.delete()
    return redirect('ClientContact')





