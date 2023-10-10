# Generated by Django 4.2.5 on 2023-10-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nomeclatura', models.CharField(default='', max_length=200)),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('fecha_inicio_contrato', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('rnc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id_entidad', models.AutoField(primary_key=True, serialize=False)),
                ('entidad', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id_industria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_industria', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id_operacion', models.AutoField(primary_key=True, serialize=False)),
                ('operacion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('apellido_contacto', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.IntegerField()),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='industria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.industria'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.localidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='status_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.status'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.entidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_operacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.operacion'),
        ),
    ]
