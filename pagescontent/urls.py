from django.urls import path
from . import views

urlpatterns = [
#Prueba de plantillas AdminLTE (Despues cambiar nombre de funciones)   
    path('', views.Home, name="Home"),
###########################################################################
    path('Dashboard/', views.Admin_Page_Service_Center, name="Dashboard"),
    path('Implementaciones/', views.Formularios_Implementaciones, name='Implementaciones'),
    
]


