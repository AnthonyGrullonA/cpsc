# Generated by Django 4.2.5 on 2023-09-18 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientdata', '0003_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='correo_contacto_directo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre_contacto_directo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_contacto_directo',
        ),
    ]
