from django.db import models

# Create your models here.
#En este modelo podran definirse los sectores.
class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    nombre_industria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
      
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
    
    OPTCIONES_LOCALIDAD = (
        ('NAP West', 'NAP West'),
        ('NAP East', 'NAP East'),
        ('NAP Cloud', 'NAP Cloud'),
        ('N/A', 'N/A'),
    )

    id_cliente = models.AutoField(primary_key=True)
    nomeclatura = models.CharField(max_length=200)
    nombre_empresa = models.CharField(max_length=200)
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.CharField(max_length=20, choices=OPCIONES_STATUS_CLIENTE)
    tipo_operacion = models.CharField(max_length=20, choices=OPCIONES_TIPO_OPERACION)
    tipo_entidad = models.CharField(max_length=20, choices=OPCIONES_TIPO_ENTIDAD)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
    site = models.CharField(max_length=20,choices=OPTCIONES_LOCALIDAD, default='')
 
class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=100)
