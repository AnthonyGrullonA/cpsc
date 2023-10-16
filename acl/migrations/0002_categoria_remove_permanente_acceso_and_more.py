# Generated by Django 4.2.5 on 2023-10-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='permanente',
            name='acceso',
        ),
        migrations.RemoveField(
            model_name='permanente',
            name='agregado_por',
        ),
        migrations.RemoveField(
            model_name='permanente',
            name='fecha',
        ),
        migrations.AddField(
            model_name='permanente',
            name='categoria1',
            field=models.ManyToManyField(to='acl.categoria'),
        ),
    ]
