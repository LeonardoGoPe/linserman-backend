# Generated by Django 3.2.5 on 2021-08-12 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0003_auto_20210809_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratoxsector',
            name='coordenadas_googleMaps',
        ),
        migrations.RemoveField(
            model_name='contratoxsector',
            name='ubicacion_googleMaps',
        ),
    ]
