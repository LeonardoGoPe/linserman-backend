from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .models import *
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

from rest_framework import generics

# Create your views here.

#Funcion login
@api_view(['POST'])
def login(request):
    """Método para login de usuario y obtener token"""
    correo = request.POST.get('correo')
    password = request.POST.get('password')

    try:
        user=Usuarios.objects.get(correo=correo)
        usuario=Usuarios.objects.get(id=user.id)
    except Usuarios.DoesNotExist:
        return Response({'data':"Usuario no válido",'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    pwd_valid = check_password(password,user.password)
    if not pwd_valid:
        return Response({'data':"Contraseña no válida",'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'data':{
        'token':token.key,
        'nombres':user.nombres,
        'apellidos':user.apellidos,
        'tipo_usuario':usuario.tipo_usuario,
    },'code':status.HTTP_200_OK},status.HTTP_200_OK)


#Usuarios
@api_view(['GET', 'POST'])
def usuarios(request):
    """Método para obtener los usuarios y crear un nuevo usuario"""
    permission_classes = [IsAuthenticated]

    if request.method == 'GET':
        #print(request.query_params)
        if len(request.query_params) == 0:
            usuarios = Usuarios.objects.all()
            serializer = UsuariosSerializer(usuarios, many=True)
            return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)
        
        else:
            usuarios = Usuarios.objects.all()
            tipo_usuario = request.query_params.get('tipo_usuario')
            if usuarios is not None:
                usuarios_filtrados = usuarios.filter(tipo_usuario=tipo_usuario)
                serializer = UsuariosSerializer(usuarios_filtrados, many=True)
                #print(serializer)
            return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response({'data':serializer.data,'code':status.HTTP_201_CREATED},status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

#Usuario
@api_view(['GET', 'PUT', 'DELETE'])
def usuario(request, pk):
    """Método para obtener, actualizar o eliminar un usuario"""
    permission_classes = [IsAuthenticated]

    try:
        usuario = Usuarios.objects.get(pk=pk)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuariosSerializer(usuario)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UsuariosSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_202_ACCEPTED},status.HTTP_202_ACCEPTED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response({'data':'Eliminación exitosa','code':status.HTTP_204_NO_CONTENT},status.HTTP_204_NO_CONTENT)


#Actividades
@api_view(['GET', 'POST'])
def actividades(request):
    """Método para obtener las actividades y crear una nueva actividad"""
    permission_classes = [IsAuthenticated]

    if request.method == 'GET':
        actividades = Actividad.objects.all()
        serializer = ActividadesSerializer(actividades, many=True)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ActividadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_201_CREATED},status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

#Actividad
@api_view(['GET', 'PUT', 'DELETE'])
def actividad(request, pk):
    """Método para obtener, actualizar o eliminar una actividad"""
    permission_classes = [IsAuthenticated]

    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActividadesSerializer(actividad)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ActividadesSerializer(actividad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_202_ACCEPTED},status.HTTP_202_ACCEPTED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        actividad.delete()
        return Response({'data':'Eliminación exitosa','code':status.HTTP_204_NO_CONTENT})


#Sectores
@api_view(['GET', 'POST'])
def sectores(request):
    """Método para obtener los sectores y crear un nuevo sector"""
    permission_classes = [IsAuthenticated]

    if request.method == 'GET':
        sectores = Sector.objects.all()
        serializer = SectoresSerializer(sectores, many=True)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SectoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_201_CREATED},status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

#Sector
@api_view(['GET', 'PUT', 'DELETE'])
def sector(request, pk):
    """Método para obtener, actualizar o eliminar un sector"""
    permission_classes = [IsAuthenticated]

    try:
        sector = Sector.objects.get(pk=pk)
    except Sector.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SectoresSerializer(sector)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SectoresSerializer(sector, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_202_ACCEPTED},status.HTTP_202_ACCEPTED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sector.delete()
        return Response({'data':'Eliminación exitosa','code':status.HTTP_204_NO_CONTENT})


#Contratos
@api_view(['GET', 'POST'])
def contratos(request):
    """Método para obtener los contratos y crear un nuevo contrato"""
    permission_classes = [IsAuthenticated]

    if request.method == 'GET':
        contratos = Contrato.objects.all()
        serializer = ContratosSerializer(contratos, many=True)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        actividades = []
        sectores = []
        usuarios = []
        contrato = {}

        #Crear registros en tabla SectorXActividad
        for sector in request.data['sectores']:
            #print(sector['sector_data'])

            for actividad in sector['actividades']:
                actividad_data = Actividad.objects.get(pk=actividad)
                actividad_instance = SectorXActividad.objects.create(actividad_data=actividad_data)
                actividades.append(actividad_instance)
        
        #Crear registros en tabla ContratoXSector
        for sector in request.data['sectores']:
            sector_data = Sector.objects.get(pk=sector['sector_data'])
            sector_instance = ContratoXSector.objects.create(
                sector_data = sector_data
            )

            #Setear objetos actividades
            for actividad in actividades:
                sector_instance.actividades.add(actividad)
            
            sectores.append(sector_instance)

        #Obtener data de usuarios
        for usuario in request.data['usuarios']:
            usuario_data = Usuarios.objects.get(pk=usuario)
            usuarios.append(usuario_data)

        #Crear registro en contrato
        contrato_instance = Contrato.objects.create(
            descripcion = request.data['descripcion'],
            nombre_contrato = request.data['nombre_contrato']
        )

        #Setear objetos usuarios y sectores
        for usuario in usuarios:
                contrato_instance.usuarios.add(usuario)

        for sector in sectores:
                contrato_instance.sectores.add(sector)

        print(contrato)

        #print(request.data)
        #print(serializerFin)
        serializer = ContratosSerializer(data=contrato)
        if serializer.is_valid():
            #print(serializer)
            return Response({'data':serializer.data,'code':status.HTTP_201_CREATED},status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

#class UsuariosViewSet(viewsets.ModelViewSet):
#    """Manejo de usuarios"""
#    serializer_class = UsuariosSerializer
#    queryset = Usuarios.objects.all()
