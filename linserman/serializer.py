
from os import write
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class UsuariosSerializer(serializers.ModelSerializer):
    """Serializamos el perfil del usuario"""

    empresa = EmpresaSerializer(read_only=True)

    class Meta:
        model = Usuarios
        fields = ['id','cedula','correo','nombres','apellidos','direccion','tipo_usuario','password','empresa','is_active']
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
            empresa = Empresa(id_empresa=validated_data['empresa']),
            password = validated_data['password'],
        )

        return user


class SectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class ContratoXSectorSerializer(serializers.ModelSerializer):
    sector_data = SectoresSerializer(read_only=True)
    actividades = ActividadesSerializer(many=True, read_only=True)
    usuarios_fiscalizadores = UsuariosSerializer(many=True, read_only=True)
    usuarios_supervisores = UsuariosSerializer(many=True, read_only=True)

    class Meta:
        model = ContratoXSector
        fields = '__all__'

class ContratosSerializer(serializers.ModelSerializer):
    sectores = ContratoXSectorSerializer(many=True, read_only=True)

    class Meta:
        model = Contrato
        fields = '__all__'
