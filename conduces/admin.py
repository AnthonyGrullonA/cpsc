from django.contrib import admin
from .models import (
    inventarioSinFirmar,
    ConduceEntrada,
    conduceEntradaRealizado,
    inventarioFirmado,
    ConduceSalida,
    AprobacionAduanal,
    conduceSalidaRealizado,
    inventarioF,
)

# Registra los modelos en el panel de administración
admin.site.register(inventarioSinFirmar)
admin.site.register(ConduceEntrada)
admin.site.register(conduceEntradaRealizado)
admin.site.register(inventarioFirmado)
admin.site.register(ConduceSalida)
admin.site.register(AprobacionAduanal)
admin.site.register(conduceSalidaRealizado)
admin.site.register(inventarioF)
