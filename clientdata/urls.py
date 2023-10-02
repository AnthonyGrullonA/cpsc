from django.urls import path
from . import views

urlpatterns = [
    path('ClientContact/', views.Client_Contact_View, name='ClientContact'),
    path('ClientList/', views.Client_List_View, name='ClientList'),
    path('registrarCliente/', views.RegistrarClientes)
]
