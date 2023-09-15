from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.

#El home carga el login 1
def Home(request):
    return render(request, 'home.html')


def Admin_Page_Service_Center(request):
    return render(request, 'admin_template/index.html')


def Industry_View(request):
    return render(request, 'pages/bank_info/industry.html')


def Services_View(request):
    return render(request, 'pages/bank_info/service.html')


def Client_Contact_View(request):
    return render(request, 'pages/client_control/client_contact.html')


def Client_List_View(request):
    return render(request, 'pages/client_control/client_list.html')


def Service_Order_VIew(request):
    return render(request, 'pages/client_control/service_order.html')


def Input_Conduce_View(request):
    return render(request, 'pages/conduces/entrada.html')


def Output_Conduce_View(request):
    return render(request, 'pages/conduces/salida.html')


def Acl_Permanent_View(request):
    return render(request, 'pages/cosmos/acl_permanent.html')


def Acl_Temporary_View(request):
    return render(request, 'pages/cosmos/acl_temporary.html')


def Restridted_Client_View(request):
    return render(request, 'pages/cosmos/restridted_client.html')


def Calendar_view(request):
    return render(request, 'pages/time_c/calendar.html')


def Task_List_View(request):
    return render(request, 'pages/time_c/task_list.html')

#Prueba de plantillas AdminLTE (Despues cambiar nombre de funciones)

def adminvacio(request):
    return render(request, 'admin_template/starter.html')

