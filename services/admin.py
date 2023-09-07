from django.contrib import admin
from .models import servicios, Cliente

# Registra los modelos en el panel de administración
admin.site.register(servicios)
admin.site.register(Cliente)
