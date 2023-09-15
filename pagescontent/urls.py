from django.urls import path
from . import views

urlpatterns = [
#Prueba de plantillas AdminLTE (Despues cambiar nombre de funciones)   
    path('DashboardV/', views.adminvacio, name='PRUEBA 2'),
###########################################################################
    path('', views.Home, name="Home"),
    path('Dashboard/', views.Admin_Page_Service_Center, name="Dashboard"),
    path('industry/', views.Industry_View, name="Industry"),
    path('service/', views.Services_View, name='Services'),
    path('ClientContact/', views.Client_Contact_View, name='ClientContact'),
    path('ClientList/', views.Client_List_View, name='ClientList'),
    path('ServiceOrder/', views.Service_Order_VIew, name='ServiceOrder'),
    path('ConduceEntrada/', views.Input_Conduce_View, name='ConduceEntrada'),
    path('ConduceSalida', views.Output_Conduce_View, name='ConduceSalida'),
    path('acl/', views.Acl_Permanent_View, name='ACL'),
    path('acl_temp/', views.Acl_Temporary_View, name='ACL_TEMP'),
    path('Clientes_R/', views.Restridted_Client_View, name='ClientesRestringidos'),
    path('Calendario/', views.Calendar_view, name='Calendario'),
    path('Task/', views.Task_List_View, name='TaskList'),
    
]
