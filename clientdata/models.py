from django.db import models

# Create your models here.

class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_industria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_industria
    
    
class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.status
      
      
class Operacion(models.Model):
    id_operacion = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    operacion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.operacion


class Entidad(models.Model):
    id_entidad = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    entidad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.entidad
    

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    localidad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.localidad
    
class Cliente(models.Model):

    id_cliente = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nomeclatura = models.CharField(max_length=200, default='')
    nombre_empresa = models.CharField(max_length=200)
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.ForeignKey(Status, on_delete=models.PROTECT)
    tipo_operacion = models.ForeignKey(Operacion, on_delete=models.PROTECT)
    tipo_entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)
    industria = models.ForeignKey(Industria, on_delete=models.PROTECT)
    site = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre_empresa
    
    
class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50)
    empresa = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
