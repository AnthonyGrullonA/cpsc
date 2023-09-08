from django.db import models

# Create your models here.
#En este modelo podran definirse los sectores.
class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    nombre_industria = models.CharField(max_length=100)
      
class Cliente(models.Model):
    OPCIONES_STATUS_CLIENTE = (
        ('activo', 'Cliente Activo'),
        ('inactivo', 'Cliente Inactivo'),
    )
    
    OPCIONES_TIPO_OPERACION = (
        ('contingencia', 'Contingencia'),
        ('primario', 'Primario'),
    )
    
    OPCIONES_TIPO_ENTIDAD = (
        ('publico', 'Público'),
        ('privado', 'Privado'),
    )

    id_cliente = models.AutoField(primary_key=True)
    nomeclatura = models.CharField(max_length=200)
    nombre_empresa = models.CharField(max_length=200)
    nombre_contacto_directo = models.CharField(max_length=200)
    correo_contacto_directo = models.EmailField(unique=True)
    telefono_contacto_directo = models.CharField(max_length=15, blank=True, null=True)
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.CharField(max_length=20, choices=OPCIONES_STATUS_CLIENTE)
    tipo_operacion = models.CharField(max_length=20, choices=OPCIONES_TIPO_OPERACION)
    tipo_entidad = models.CharField(max_length=20, choices=OPCIONES_TIPO_ENTIDAD)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
 