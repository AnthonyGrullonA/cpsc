from django.contrib import admin
from .models import Industria, Cliente

# Registra los modelos en el panel de administración
admin.site.register(Industria)
admin.site.register(Cliente)
