# Generated by Django 4.2.5 on 2023-10-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AprobacionAduanal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='conduceEntradaRealizado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='conduceSalidaRealizado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='inventarioSinFirmar',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inventarioFirmado',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('conduce_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conduces.conduceentradarealizado')),
            ],
        ),
        migrations.CreateModel(
            name='inventarioF',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('conduce_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conduces.conduceentradarealizado')),
                ('conduce_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conduces.conducesalidarealizado')),
            ],
        ),
        migrations.CreateModel(
            name='ConduceSalida',
            fields=[
                ('id_conduce_entrada', models.AutoField(primary_key=True, serialize=False)),
                ('statusc', models.CharField(default='Salida', max_length=10)),
                ('direccion', models.CharField(default='Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D', max_length=150)),
                ('Telefono', models.CharField(default='809-566-3495', max_length=150)),
                ('rnc1', models.CharField(default='RNC.1-30-26091-5 [S.A]', max_length=50)),
                ('rnc2', models.CharField(default='RNC.1-30-48300-2 [INC]', max_length=50)),
                ('nombre_empresa', models.CharField(default='NAP Del Caribe', max_length=50)),
                ('fecha_salida', models.DateField()),
                ('notas', models.CharField(max_length=255)),
                ('nombre_representante_cliente', models.CharField(max_length=100)),
                ('documento_identidad_cliente', models.CharField(max_length=50)),
                ('empresa_cliente', models.CharField(max_length=50)),
                ('nombre_empleado_napc', models.CharField(max_length=100)),
                ('inventario_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conduces.inventariofirmado')),
            ],
        ),
        migrations.CreateModel(
            name='ConduceEntrada',
            fields=[
                ('id_conduce_entrada', models.AutoField(primary_key=True, serialize=False)),
                ('statusc', models.CharField(default='Entrada', max_length=10)),
                ('direccion', models.CharField(default='Av. Lope de Vega #19, Edif. PIISA, Bloque A, Suite 401 Naco, Santo Domingo, R.D', max_length=150)),
                ('Telefono', models.CharField(default='809-566-3495', max_length=150)),
                ('rnc1', models.CharField(default='RNC.1-30-26091-5 [S.A]', max_length=50)),
                ('rnc2', models.CharField(default='RNC.1-30-48300-2 [INC]', max_length=50)),
                ('nombre_empresa', models.CharField(default='NAP Del Caribe', max_length=50)),
                ('fecha_entrada', models.DateField()),
                ('notas', models.CharField(max_length=255)),
                ('nombre_representante_cliente', models.CharField(max_length=100)),
                ('documento_identidad_cliente', models.CharField(max_length=50)),
                ('empresa_cliente', models.CharField(max_length=50)),
                ('nombre_empleado_napc', models.CharField(max_length=100)),
                ('inventario_sf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conduces.inventariosinfirmar')),
            ],
        ),
    ]
