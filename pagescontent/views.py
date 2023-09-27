from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

#El home carga el login 1
def Home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')  
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
    return render(request, 'home.html')


# 404 error template
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

######################################################################################################################################################

@login_required
def Admin_Page_Service_Center(request):
    return render(request, 'admin_template/index.html')

@login_required
def Industry_View(request):
    return render(request, 'pages/bank_info/industry.html')

@login_required
def Services_View(request):
    return render(request, 'pages/bank_info/service.html')

@login_required
def Client_Contact_View(request):
    return render(request, 'pages/client_control/client_contact.html')

@login_required
def Client_List_View(request):
    return render(request, 'pages/client_control/client_list.html')

@login_required
def Service_Order_VIew(request):
    return render(request, 'pages/client_control/service_order.html')

@login_required
def Input_Conduce_View(request):
    return render(request, 'pages/conduces/entrada.html')

@login_required
def Output_Conduce_View(request):
    return render(request, 'pages/conduces/salida.html')

@login_required
def Acl_Permanent_View(request):
    return render(request, 'pages/cosmos/acl_permanent.html')

@login_required
def Acl_Temporary_View(request):
    return render(request, 'pages/cosmos/acl_temporary.html')

@login_required
def Restridted_Client_View(request):
    return render(request, 'pages/cosmos/restridted_client.html')

@login_required
def Formularios_ACL(request):
    return render(request, 'pages/formularios/formularios_acl.html')

@login_required
def Formularios_Implementaciones(request):
    return render(request, 'pages/formularios/formularios_implementaciones.html')

@login_required
def Calendar_view(request):
    return render(request, 'pages/time_c/calendar.html')

@login_required
def Task_List_View(request):
    return render(request, 'pages/time_c/task_list.html')

