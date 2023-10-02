from django.urls import path
from . import views

urlpatterns = [
    
    path('ServiceOrder/', views.Service_Order_View, name='ServiceOrder'),


]
