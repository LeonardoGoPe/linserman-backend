# Generated by Django 3.2.5 on 2021-09-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0013_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='actividades_empresa',
        ),
        migrations.AddField(
            model_name='empresa',
            name='descripcion_empresa',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre_empresa',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ruc_empresa',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
