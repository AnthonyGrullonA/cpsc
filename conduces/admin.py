from django.contrib import admin
from . import models

# Registra los modelos en el panel de administración
admin.site.register(models.ConduceEntrada)
admin.site.register(models.ConduceSalida)
