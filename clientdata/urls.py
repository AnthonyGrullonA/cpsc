from django.urls import path
from . import views

urlpatterns = [
    path('ClientContact/', views.Client_Contact_View, name='ClientContact'),
    path('ClientList/', views.Client_List_View, name='ClientList'),
    path('registrarContacto/', views.RegistrarContactos, name='registrar_Contacto'),
    path('registrarCliente/', views.RegistrarClientes, name='registrar_cliente'),
    path('eliminarCliente/<int:id_cliente>/', views.EliminarCliente, name='eliminar_cliente'),
    path('eliminarContacto/<int:id_contacto>/', views.EliminarContacto, name='eliminar_contacto'),
]
