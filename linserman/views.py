from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .models import *
from .serializer import *

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password

# Create your views here.

#Funcion login
@api_view(['POST'])
def login(request):
    correo = request.POST.get('correo')
    password = request.POST.get('password')

    try:
        user=Usuarios.objects.get(correo=correo)
        usuario=Usuarios.objects.get(id=user.id)
    except Usuarios.DoesNotExist:
        return Response({'data':"Usuario no válido",'code':400},status=status.HTTP_400_BAD_REQUEST)

    pwd_valid = check_password(password,user.password)
    if not pwd_valid:
        return Response({'data':"Contraseña no válida",'code':400},status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'data':{
        'token':token.key,
        'nombres':user.nombres,
        'apellidos':user.apellidos,
        'tipo_usuario':usuario.tipo_usuario,
    },'code':200})

class UsuariosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuarios.objects.all()
    serializer_class = UseriosSerializer