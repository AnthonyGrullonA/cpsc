from django.db import models
from clientdata import models as cd
# Create your models here.

class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.nombre_categoria
    
class permanente(models.Model):
    id_acl = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    empresa = models.ForeignKey(cd.Cliente, on_delete=models.PROTECT)
    email = models.CharField(max_length=50)
    autorizador = models.CharField(max_length=100, db_collation='utf8mb3_spanish_ci')
    categoria = models.ManyToManyField(categoria)
    
    def __str__(self):
        return self.nombre

class Restringidos(models.Model):
    id_restringidos = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_empresa = models.ForeignKey(cd.Cliente, on_delete=models.PROTECT)
