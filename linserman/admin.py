from django.contrib import admin
from linserman import models

# Register your models here.
admin.site.register(models.Usuarios)
admin.site.register(models.Actividad)
admin.site.register(models.Sector)
admin.site.register(models.Contrato)
admin.site.register(models.ContratoXSector)
admin.site.register(models.SectorXActividad)
