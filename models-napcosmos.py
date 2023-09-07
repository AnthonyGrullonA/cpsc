# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acl(models.Model):
    id_acl = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    acceso = models.CharField(max_length=25)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'acl'
        db_table_comment = 'Tabla con el ACL de los clientes'


class AclTemporal(models.Model):
    id_acl_temp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    apellido = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    email = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    autorizador = models.CharField(max_length=100)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tecn_noc = models.CharField(max_length=50, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'acl_temporal'
        db_table_comment = 'Tabla con el ACL de los clientes'


class Acls(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    acceso = models.CharField(max_length=25)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'acls'
        db_table_comment = 'Tabla con el ACL de los clientes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50)
    tipo_empresa = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    restringido = models.CharField(max_length=10)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'empresas'
        db_table_comment = 'Tabla de los Clientes/Empresas'


class GridLocation(models.Model):
    id_grid_location = models.AutoField(primary_key=True)
    num_gabinete = models.CharField(max_length=20)
    cliente = models.CharField(max_length=75)
    grid_location = models.CharField(max_length=75)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'grid_location'
        db_table_comment = 'Tabla que guarda los Grid Location'


class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    personal = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100)
    grid_location = models.CharField(max_length=60)
    firma = models.TextField()
    hora_sal = models.CharField(max_length=25)
    fecha_sal = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    empleado_ent = models.CharField(max_length=25)
    fecha_ret = models.DateTimeField()
    empleado_ret = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'historial'
        db_table_comment = 'Formulario Registro'


class HistorialSoc(models.Model):
    id_hist_soc = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=75)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    carnet = models.CharField(max_length=50)
    personal_ent = models.CharField(max_length=50)
    fecha_ent = models.CharField(max_length=30)
    personal_rec = models.CharField(max_length=50)
    fecha_rec = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_soc'


class HistorialSocOld(models.Model):
    id_hist_soc = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=75)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    carnet = models.CharField(max_length=50)
    personal_ent = models.CharField(max_length=50)
    fecha_ent = models.CharField(max_length=30)
    personal_rec = models.CharField(max_length=50)
    fecha_rec = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_soc_old'


class LlavesActivas(models.Model):
    id_activas = models.AutoField(primary_key=True)
    grid_location = models.CharField(max_length=150)
    fecha_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llaves_activas'
        db_table_comment = 'Tabla que contiene las llaves que estan activas actualmente'


class LlavesInternas(models.Model):
    id_llaves_int = models.AutoField(primary_key=True)
    num_gabinete = models.IntegerField()
    cliente = models.CharField(max_length=75)
    grid_location = models.CharField(max_length=75)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llaves_internas'
        db_table_comment = 'Tabla que guarda los Grid Location'


class LlavesInternasa(models.Model):
    id_llaves_int = models.AutoField(primary_key=True)
    num_gabinete = models.IntegerField()
    cliente = models.CharField(max_length=75)
    grid_location = models.CharField(max_length=75)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'llaves_internasa'
        db_table_comment = 'Tabla que guarda los Grid Location'


class Logs(models.Model):
    id_log = models.AutoField(primary_key=True)
    proceso = models.CharField(max_length=150, db_collation='latin1_spanish_ci')
    accion = models.CharField(max_length=250, db_collation='latin1_spanish_ci')
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logs'


class NwAcl(models.Model):
    id_acl = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    acceso = models.CharField(max_length=25)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_acl'
        db_table_comment = 'Tabla con el ACL de los clientes en NAP West'


class NwAclTemporal(models.Model):
    id_acl_temp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    apellido = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    cedula = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    email = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    autorizador = models.CharField(max_length=100)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tecn_noc = models.CharField(max_length=50, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'nw_acl_temporal'
        db_table_comment = 'Tabla con el ACL de los clientes temporales en el NAP West'


class NwEmpresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50)
    tipo_empresa = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    restringido = models.CharField(max_length=10)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_empresas'
        db_table_comment = 'Tabla de los Clientes/Empresas en el NAP West'


class NwGridLocation(models.Model):
    id_grid_location = models.AutoField(primary_key=True)
    num_gabinete = models.CharField(max_length=20)
    cliente = models.CharField(max_length=75)
    grid_location = models.CharField(max_length=75)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_grid_location'
        db_table_comment = 'Tabla que guarda los Grid Location en NAP West'


class NwHistorial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    personal = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100)
    grid_location = models.CharField(max_length=60)
    firma = models.TextField()
    hora_sal = models.CharField(max_length=25)
    fecha_sal = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    empleado_ent = models.CharField(max_length=25)
    fecha_ret = models.DateTimeField()
    empleado_ret = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'nw_historial'
        db_table_comment = 'Formulario Registro en NAP West'


class NwLlavesActivas(models.Model):
    id_activas = models.AutoField(primary_key=True)
    grid_location = models.CharField(max_length=150)
    fecha_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_llaves_activas'
        db_table_comment = 'Tabla que contiene las llaves que estan activas actualmente el NAP West'


class NwLlavesInternas(models.Model):
    id_llaves_int = models.AutoField(primary_key=True)
    num_gabinete = models.IntegerField()
    cliente = models.CharField(max_length=75)
    grid_location = models.CharField(max_length=75)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_llaves_internas'
        db_table_comment = 'Tabla que guarda las llaves internas del NAP West'


class NwRestringidos(models.Model):
    id_restringidos = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50)
    tipo_empresa = models.CharField(max_length=25)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_restringidos'
        db_table_comment = 'Clientes restringidos del NAP West'


class NwSalidaLlaves(models.Model):
    id_salida_llaves = models.AutoField(primary_key=True)
    personal = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    grid_location = models.CharField(max_length=125)
    fecha = models.DateTimeField()
    firma = models.TextField()
    empleado_nap = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'nw_salida_llaves'
        db_table_comment = 'Tabla con los registros de las llaves que se entregaron a los clientes en NAP West'


class NwTecnicoNoc(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nw_tecnico_noc'
        db_table_comment = 'Tecnico NAP West'


class RegistroSoc(models.Model):
    id_reg_soc = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=75)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    carnet = models.CharField(max_length=50)
    personal_soc = models.CharField(max_length=50)
    fecha_ent = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registro_soc'


class ReporteSemanal(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    personal = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100)
    grid_location = models.CharField(max_length=150)
    fecha = models.DateTimeField()
    firma = models.TextField()
    empleado_nap = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'reporte_semanal'
        db_table_comment = 'Tabla con los registros de las llaves que se entregaron a los clientes'


class Restringidos(models.Model):
    id_restringidos = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50)
    tipo_empresa = models.CharField(max_length=25)
    agregado_por = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'restringidos'


class SalidaLlaves(models.Model):
    id_salida_llaves = models.AutoField(primary_key=True)
    personal = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    grid_location = models.CharField(max_length=125)
    fecha = models.DateTimeField()
    firma = models.TextField()
    empleado_nap = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'salida_llaves'
        db_table_comment = 'Tabla con los registros de las llaves que se entregaron a los clientes'


class TecnicoNoc(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tecnico_noc'


class Usuarios(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField()
    admin = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'usuarios'
