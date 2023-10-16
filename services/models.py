from django.db import models
from clientdata.models import Cliente
# Create your models here.

class servicios(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_servicio

class status(models.Model):
    id_status = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    estado_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.estado_status
    
class Ordenes_De_Servicio(models.Model):
    id_ods = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    clientes = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servicio_contratado = models.ForeignKey(servicios, on_delete=models.PROTECT)
    nomeclatura_ods = models.CharField(max_length=100, default='NOT DEFINED')
    status = models.ForeignKey(status, on_delete=models.PROTECT)
    fecha_inicio = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Orden de Servicio: {self.nomeclatura_ods}" 

