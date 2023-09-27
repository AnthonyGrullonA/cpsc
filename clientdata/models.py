from django.db import models

# Create your models here.
#En este modelo podran definirse los sectores.
class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    nombre_industria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    
    
class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
      
      
class Operacion(models.Model):
    id_operacion = models.AutoField(primary_key=True)
    operacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)


class Entidad(models.Model):
    id_entidad = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    
    
class Cliente(models.Model):

    id_cliente = models.AutoField(primary_key=True)
    nomeclatura = models.CharField(max_length=200)
    nombre_empresa = models.CharField(max_length=200)
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.ForeignKey(Status, on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE)
    tipo_entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
    site = models.ForeignKey(Localidad, on_delete=models.CASCADE)
 
class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=100)
