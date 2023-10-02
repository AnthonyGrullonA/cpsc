from django.contrib import admin
from . import models

# Registra los modelos en el panel de administración
admin.site.register(models.Industria)

admin.site.register(models.Status)

admin.site.register(models.Operacion)

admin.site.register(models.Entidad)

admin.site.register(models.Localidad)

admin.site.register(models.Contacto)

admin.site.register(models.Cliente)
