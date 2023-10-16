from django.db import models

# Create your models here.

class Status_Implementaciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_status = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_status
    

class Implementaciones(models.Model):
    id_implementacion = models.AutoField(primary_key=True)
    nomeclatura = models.CharField(max_length=50, blank=True)  # Puedes permitir que sea nulo o en blanco
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=200)
    status_interno = models.ForeignKey(Status_Implementaciones, on_delete=models.PROTECT)
    
        
    def __str__(self):
        return self.nomeclatura