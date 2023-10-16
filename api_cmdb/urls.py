from django.urls import path
from . import views
urlpatterns = [
    path('Implementaciones/', views.Implementaciones_view, name='Implementaciones'),
    path('POST_CMDB', views.POST_CMDB_VIEW, name='CMDB'),
]
