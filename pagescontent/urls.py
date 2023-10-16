from django.urls import path
from . import views

urlpatterns = [
#Prueba de plantillas AdminLTE (Despues cambiar nombre de funciones)   
    path('', views.login_view, name="Home"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view2, name='login'),
###########################################################################
    path('Dashboard/', views.Admin_Page_Service_Center, name="Dashboard"),
    
]


