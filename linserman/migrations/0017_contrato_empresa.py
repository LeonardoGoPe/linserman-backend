# Generated by Django 3.2.5 on 2021-10-20 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linserman', '0016_usuarios_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='linserman.empresa'),
            preserve_default=False,
        ),
    ]
