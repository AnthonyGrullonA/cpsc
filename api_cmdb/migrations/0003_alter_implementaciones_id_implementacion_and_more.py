# Generated by Django 4.2.5 on 2023-10-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_cmdb', '0002_alter_implementaciones_id_implementacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementaciones',
            name='id_implementacion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='implementaciones',
            name='nomeclatura',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
