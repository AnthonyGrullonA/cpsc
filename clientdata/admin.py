from django.contrib import admin
from .models import Industria, TipoDeEntidad, TipoDeOperacion, Cliente

# Registra los modelos en el panel de administración
admin.site.register(Industria)
admin.site.register(TipoDeEntidad)
admin.site.register(TipoDeOperacion)
admin.site.register(Cliente)
