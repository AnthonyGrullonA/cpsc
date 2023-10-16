# Generated by Django 4.2.5 on 2023-10-12 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conduces', '0002_inventario_inventario_salida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conduceentrada',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conducesalida',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario_salida',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]