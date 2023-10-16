from django.urls import path
from . import views
urlpatterns = [
    
    path('acl_form/', views.Formularios_ACL, name='FormACL'),
    path('acl_permanente/', views.Permanente_Views, name='PermanenteACL'),
    path('acl_restringido/', views.Restringido_Views, name='RestringidoACL'),
    path('acl_temporal/', views.Temporal_Views, name='TemporalACL'),
]
