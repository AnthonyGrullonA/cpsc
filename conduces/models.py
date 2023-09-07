from django.db import models

class inventarioSinFirmar(models.Model):
    #items conduce
    id_inventario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    cantidad = models.IntegerField()

class ConduceEntrada(models.Model):
    id_conduce_entrada = models.AutoField(primary_key=True)
    statusc = models.CharField(max_length=10, default="Entrada")
    direccion = models.CharField(max_length=150, default="Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D")
    Telefono = models.CharField(max_length=150, default="809-566-3495")
    rnc1 = models.CharField(max_length=50, default="RNC.1-30-26091-5 [S.A]")
    rnc2= models.CharField(max_length=50, default="RNC.1-30-48300-2 [INC]")
    nombre_empresa = models.CharField(max_length=50, default="NAP Del Caribe")
    fecha_entrada = models.DateField()    
    notas = models.CharField(max_length=255)
    #Relacion con inventario de entrada (Sin firmar por aduantas, luego de proceso se tendra que aprobar [Explicacion de logica])
    inventario_sf = models.ForeignKey(inventarioSinFirmar, on_delete=models.CASCADE)
    #Personal Autorizado
    nombre_representante_cliente = models.CharField(max_length=100)
    documento_identidad_cliente = models.CharField(max_length=50)
    empresa_cliente = models.CharField(max_length=50)
    nombre_empleado_napc = models.CharField(max_length=100)

class conduceEntradaRealizado(models.Model):
    id = models.AutoField(primary_key=True)
    
#Modelo de inventario sin aprobar. Logica de aprobacion pendiente
class inventarioFirmado(models.Model):
    #items conduce
    id_inventario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    conduce_entrada = models.ForeignKey(conduceEntradaRealizado, on_delete=models.CASCADE)
    # ...
class ConduceSalida(models.Model):
    id_conduce_entrada = models.AutoField(primary_key=True)
    statusc = models.CharField(max_length=10, default="Salida")
    direccion = models.CharField(max_length=150, default="Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D")
    Telefono = models.CharField(max_length=150, default="809-566-3495")
    rnc1 = models.CharField(max_length=50, default="RNC.1-30-26091-5 [S.A]")
    rnc2= models.CharField(max_length=50, default="RNC.1-30-48300-2 [INC]")
    nombre_empresa = models.CharField(max_length=50, default="NAP Del Caribe")
    fecha_salida = models.DateField()    
    notas = models.CharField(max_length=255)
    #Relacion con inventario de equipos dentro del site (Firmado por aduanas)
    inventario_f = models.ForeignKey(inventarioFirmado, on_delete=models.CASCADE)
    #Personal Autorizado
    nombre_representante_cliente = models.CharField(max_length=100)
    documento_identidad_cliente = models.CharField(max_length=50)
    empresa_cliente = models.CharField(max_length=50)
    nombre_empleado_napc = models.CharField(max_length=100)

    
class AprobacionAduanal(models.Model):
    id = models.AutoField(primary_key=True)
    pass

#CONDUCE REALIZADOS
    
class conduceSalidaRealizado(models.Model):
    id = models.AutoField(primary_key=True)

class inventarioF(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    conduce_entrada = models.ForeignKey(conduceEntradaRealizado, on_delete=models.CASCADE)
    conduce_salida = models.ForeignKey(conduceSalidaRealizado, on_delete=models.CASCADE)
    #El status indicara si esta dentro o no
    status = models.CharField(max_length=20)
    #logica condicional del status (si tiene conduce de salida REALIZADO[La tabla de realizado es para los firmados])