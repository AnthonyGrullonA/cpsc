from django.db import models
from clientdata import models as clientdata
# Create your models here.

class servicios(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)

class Cliente(models.Model):
    id_sc = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(clientdata.Cliente, on_delete=models.CASCADE)
    servicio_contratado = models.ForeignKey(servicios, on_delete=models.CASCADE)
