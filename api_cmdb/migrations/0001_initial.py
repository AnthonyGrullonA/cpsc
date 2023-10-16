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
            name='Status_Implementaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Implementaciones',
            fields=[
                ('id_implementacion', models.AutoField(primary_key=True, serialize=False)),
                ('nomeclatura', models.CharField(blank=True, max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.cliente')),
                ('status_interno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_cmdb.status_implementaciones')),
            ],
        ),
    ]
