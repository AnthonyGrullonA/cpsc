from django.db import models
from clientdata import models as cd

class ConduceEntrada(models.Model):
    id_conduce_entrada = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    statusc = models.CharField(max_length=10, default="Entrada")
    direccion = models.CharField(max_length=150, default="Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D")
    Telefono = models.CharField(max_length=150, default="809-566-3495")
    rnc1 = models.CharField(max_length=50, default="RNC.1-30-26091-5 [S.A]")
    rnc2= models.CharField(max_length=50, default="RNC.1-30-48300-2 [INC]")
    nombre_empresa = models.CharField(max_length=50, default="NAP Del Caribe")
    fecha_entrada = models.DateField()    
    notas = models.CharField(max_length=255)
    #Personal Autorizado
    nombre_representante_cliente = models.CharField(max_length=100)
    documento_identidad_cliente = models.CharField(max_length=50)
    empresa_cliente = models.ForeignKey(cd.Cliente, on_delete=models.PROTECT)
    nombre_empleado_napc = models.CharField(max_length=100)


class ConduceSalida(models.Model):
    id_conduce_salida = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    statusc = models.CharField(max_length=10, default="Salida")
    direccion = models.CharField(max_length=150, default="Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D")
    Telefono = models.CharField(max_length=150, default="809-566-3495")
    rnc1 = models.CharField(max_length=50, default="RNC.1-30-26091-5 [S.A]")
    rnc2= models.CharField(max_length=50, default="RNC.1-30-48300-2 [INC]")
    nombre_empresa = models.CharField(max_length=50, default="NAP Del Caribe")
    fecha_salida = models.DateField()    
    notas = models.CharField(max_length=255)
    #Personal Autorizado
    nombre_representante_cliente = models.CharField(max_length=100)
    documento_identidad_cliente = models.CharField(max_length=50)
    empresa_cliente = models.ForeignKey(cd.Cliente, on_delete=models.PROTECT)
    nombre_empleado_napc = models.CharField(max_length=100)

class Inventario(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_equipo = models.CharField(max_length=30)
    modelo_equipo = models.CharField(max_length=30)
    descripcion_equipo = models.CharField(max_length=100)
    conduce_entrada = models.ForeignKey(ConduceEntrada, on_delete=models.PROTECT)
    
class Inventario_Salida(models.Model):
    id_equipo_salida = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_equipo = models.CharField(max_length=30)
    modelo_equipo = models.CharField(max_length=30)
    descripcion_equipo = models.CharField(max_length=100)
    conduce_salida = models.ForeignKey(ConduceSalida, on_delete=models.PROTECT)
    
    
    