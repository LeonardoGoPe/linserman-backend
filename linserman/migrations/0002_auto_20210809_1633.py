# Generated by Django 3.2.5 on 2021-08-09 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratoXSector',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordenadas_googleMaps', models.CharField(max_length=512)),
                ('ubicacion_googleMaps', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SectorXActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linserman.actividad')),
            ],
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='id_actividades',
        ),
        migrations.AddField(
            model_name='contrato',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='id_sector',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='contrato',
            name='id_usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CoordenadasContratos',
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='id_actividad',
            field=models.ManyToManyField(to='linserman.SectorXActividad'),
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='id_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linserman.sector'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='id_sector',
            field=models.ManyToManyField(to='linserman.ContratoXSector'),
        ),
    ]
