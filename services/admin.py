from django.contrib import admin
from .models import servicios, status, Ordenes_De_Servicio

# Registra los modelos en el panel de administración
admin.site.register(servicios)
admin.site.register(status)
admin.site.register(Ordenes_De_Servicio)

