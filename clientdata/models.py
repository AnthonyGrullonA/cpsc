from django.db import models

#Logica de nomeclatura
class nomeclatura(models.Model):
    pass
# Create your models here.
#En este modelo podran definirse los sectores.
class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    nombre_industria = models.CharField(max_length=100)

class TipoDeEntidad(models.Model):
    OPCIONES_TIPO_ENTIDAD = (
        ('publico', 'Público'),
        ('privado', 'Privado'),
    )

    id_entidad = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=OPCIONES_TIPO_ENTIDAD)

class TipoDeOperacion(models.Model):
    OPCIONES_TIPO_OPERACION = (
        ('contingencia', 'Contingencia'),
        ('primario', 'Primario'),
    )

    id_operacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, choices=OPCIONES_TIPO_OPERACION)
    
      
class Cliente(models.Model):
    OPCIONES_STATUS_CLIENTE = (
        ('activo', 'Cliente Activo'),
        ('primario', 'Cliente Primario'),
    )
    id_cliente = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=200)
    nombre_contacto_directo = models.CharField(max_length=200)
    correo_contacto_directo = models.EmailField(unique=True)
    telefono_contacto_directo = models.CharField(max_length=15, blank=True, null=True)
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.CharField(max_length=10, choices=OPCIONES_STATUS_CLIENTE)
    tipo_operacion = models.ForeignKey(TipoDeOperacion, on_delete=models.CASCADE)
    tipo_entidad = models.ForeignKey(TipoDeEntidad, on_delete=models.CASCADE)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
 