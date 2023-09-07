from django.contrib import admin

# Importar los modelos
from .models import *

# Registrar los modelos en el admin
admin.site.register(Acl)
admin.site.register(AclTemporal)
admin.site.register(Acls)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
# admin.site.register(DjangoAdminLog)
# admin.site.register(DjangoContentType)
# admin.site.register(DjangoMigrations)
# admin.site.register(DjangoSession)
admin.site.register(Empresas)
admin.site.register(GridLocation)
admin.site.register(Historial)
admin.site.register(HistorialSoc)
admin.site.register(HistorialSocOld)
admin.site.register(LlavesActivas)
admin.site.register(LlavesInternas)
admin.site.register(LlavesInternasa)