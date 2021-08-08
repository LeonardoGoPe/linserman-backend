from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db.models.deletion import CASCADE


# Modelos

TIPOS_USUARIOS =(
    (1, "Supervisor"),
    (2, "Fiscalizador"),
    (3, "Administrador"),
)

class Actividad(models.Model):
   id_actividad = models.AutoField(primary_key=True)
   nemonico_actividad = models.CharField(max_length=255)
   texto_descripcion = models.CharField(max_length=255)


class Sector(models.Model):
   id_sector= models.AutoField(primary_key=True)
   ciudad = models.CharField(max_length=255)
   sector = models.CharField(max_length=255)
   punto_cardinal = models.CharField(max_length=255)


class Contrato(models.Model):
   id = models.AutoField(primary_key=True)
   id_actividades = models.ForeignKey(Actividad, on_delete=models.CASCADE)
   id_sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
   id_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class CoordenadasContratos(models.Model):
   id_coordenada = models.AutoField(primary_key=True)
   id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
   coordenadas_googleMaps = models.CharField(max_length=255)
   ubicacion_googleMaps = models.CharField(max_length=255)



class UsuariosManager(BaseUserManager):
   """Manager para perfiles de usuarios"""

   def create_user(self,correo,nombres,apellidos,password=None):
      """Crear nuevo Usuario"""
      if not correo:
         raise ValueError("Usuario debe tener un correo")
      correo = self.normalize_email(correo)
      user = self.model(correo=correo,nombres=nombres,apellidos=apellidos)
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, correo, nombres, apellidos, password):
      user = self.create_user(correo,nombres,apellidos,password)
      user.is_superuser = True
      user.is_staff = True
      user.save(using=self._db)
      return user
      
class Usuarios(AbstractBaseUser, PermissionsMixin):
   """Modelo Base de datos para usuarios en el sistema"""

   correo = models.EmailField(max_length=255, unique=True)
   nombres = models.CharField(max_length=255)
   apellidos = models.CharField(max_length=255)
   cedula = models.CharField(max_length=255,unique=True)
   direccion = models.CharField(max_length=255)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   tipo_usuario = models.IntegerField(choices=TIPOS_USUARIOS, default=1)

   objects = UsuariosManager()

   USERNAME_FIELD = 'correo'
   REQUIRED_FIELDS = ['nombres','apellidos']

   def getNombreCompleto(self):
      """Obtener nombre completo del usuario"""
      return self.nombres+" "+self.apellidos

   def __str__(self):
      """Retornar cadena de usuario"""
      return self.correo
