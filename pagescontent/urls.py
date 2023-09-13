from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('Dashboard/', views.adminlte, name="Dashboard"),
    path('DashboardV/', views.adminvacio, name='PRUEBA 2')
    
]
