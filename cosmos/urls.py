from django.urls import path
from . import views
urlpatterns = [
    
    path('acl/', views.Acl_Permanent_View, name='ACL'),
    path('acl_temp/', views.Acl_Temporary_View, name='ACL_TEMP'),
    path('Clientes_R/', views.Restridted_Client_View, name='ClientesRestringidos'),
    path('acl_form/', views.Formularios_ACL, name='FormACL')

]
