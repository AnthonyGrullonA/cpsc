# Generated by Django 4.2.5 on 2023-09-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdata', '0004_remove_cliente_correo_contacto_directo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nombre_cliente',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
