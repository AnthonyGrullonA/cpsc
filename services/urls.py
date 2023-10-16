from django.urls import path
from . import views

urlpatterns = [
    
    path('ServiceOrder/', views.Service_Order_View, name='ServiceOrder'),
    path('registrarServiceOrder/', views.ServiceOrderRegisterView, name='registrar_orden_de_servicio'),
    path('eliminarOrden/<int:id_ods>/', views.EliminarOrdenView, name='eliminar_orden'),


]
