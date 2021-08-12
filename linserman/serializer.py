
from os import write
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    """Serializamos el perfil del usuario"""

    class Meta:
        model = Usuarios
        fields = ('id','cedula','correo','nombres','apellidos','direccion','tipo_usuario','password')
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }
        read_only_fields = ('created','updated')

    def create(self, validated_data):
        """Crear y retornar nuevo usuario"""
        user = Usuarios.objects.create_user(
            correo = validated_data['correo'],
            nombres = validated_data['nombres'],
            apellidos = validated_data['apellidos'],
            cedula = validated_data['cedula'],
            direccion = validated_data['direccion'],
            tipo_usuario = validated_data['tipo_usuario'],
            password = validated_data['password'],
        )

        return user

class SectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id_sector','ciudad','sector','punto_cardinal']

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id_actividad','nemonico_actividad','texto_descripcion']


class SectorXActividadSerializer(serializers.ModelSerializer):
    actividad_data = ActividadesSerializer(read_only=True)

    class Meta:
        model = SectorXActividad
        fields = ['actividad_data']

class ContratoXSectorSerializer(serializers.ModelSerializer):
    sector_data = SectoresSerializer(read_only=True)
    actividades = SectorXActividadSerializer(many=True, read_only=True)

    class Meta:
        model = ContratoXSector
        fields = ['sector_data','actividades']

class ContratosSerializer(serializers.ModelSerializer):
    usuarios = UsuariosSerializer(many=True, read_only=True)
    sectores = ContratoXSectorSerializer(many=True, read_only=True)

    class Meta:
        model = Contrato
        fields = ['usuarios','sectores','descripcion','nombre_contrato']
