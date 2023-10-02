from django.urls import path
from . import views

urlpatterns = [
    
    path('ConduceEntrada/', views.Input_Conduce_View, name='ConduceEntrada'),
    path('ConduceSalida', views.Output_Conduce_View, name='ConduceSalida'),
]
