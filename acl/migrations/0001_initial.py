# Generated by Django 4.2.5 on 2023-10-16 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=30)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restringidos',
            fields=[
                ('id_restringidos', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('nombre_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='permanente',
            fields=[
                ('id_acl', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('autorizador', models.CharField(db_collation='utf8mb3_spanish_ci', max_length=100)),
                ('categoria', models.ManyToManyField(to='acl.categoria')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.cliente')),
            ],
        ),
    ]
