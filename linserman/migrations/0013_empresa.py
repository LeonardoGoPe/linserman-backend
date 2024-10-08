# Generated by Django 3.2.5 on 2021-09-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0012_usuarios_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('ruc_empresa', models.CharField(max_length=255)),
                ('actividades_empresa', models.BooleanField(default=True)),
                ('empresaActiva', models.BooleanField(default=True)),
            ],
        ),
    ]
