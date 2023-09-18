from django.db import models
from clientdata.models import Cliente
# Create your models here.

class servicios(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)


class status(models.Model):
    id_status = models.AutoField(primary_key=True)
    estado_status = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    
    
class Ordenes_De_Servicio(models.Model):
    id_ods = models.AutoField(primary_key=True)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio_contratado = models.ForeignKey(servicios, on_delete=models.CASCADE)
    nomeclatura_ods = models.CharField(max_length=100)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()

