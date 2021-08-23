# Generated by Django 3.2.5 on 2021-08-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0006_auto_20210815_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='actividadActiva',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='contratoActivo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='contratoXSectorActivo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='sectorActivo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sectorxactividad',
            name='sectorXActividadActivo',
            field=models.BooleanField(default=True),
        ),
    ]
