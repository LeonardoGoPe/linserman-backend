# Generated by Django 3.2.5 on 2021-08-16 04:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0005_contrato_nombre_contrato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='punto_cardinal',
            new_name='zona_ciudad',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='usuarios',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='sector',
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='nombre_sector',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='usuarios_fiscalizadores',
            field=models.ManyToManyField(related_name='contratoxsector_fiscalizadores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contratoxsector',
            name='usuarios_supervisores',
            field=models.ManyToManyField(related_name='contratoxsector_supervisores', to=settings.AUTH_USER_MODEL),
        ),
    ]
