
from os import write
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *

class UseriosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'