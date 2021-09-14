from .models import *
from .serializer import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password

# Create your views here.

#Funcion login
@api_view(['POST'])
@permission_classes([AllowAny])
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
        'nombres':usuario.nombres,
        'apellidos':usuario.apellidos,
        'id':usuario.id,
        'empresa':usuario.empresa,
        'tipo_usuario':usuario.tipo_usuario,
    },'code':status.HTTP_200_OK},status.HTTP_200_OK)


#Usuarios
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def usuarios(request):
    """Método para obtener los usuarios y crear un nuevo usuario"""

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
@permission_classes([IsAuthenticated])
def usuario(request, pk):
    """Método para obtener, actualizar o eliminar un usuario"""

    try:
        usuario = Usuarios.objects.get(pk=pk)
    except Usuarios.DoesNotExist:
        return Response({'data':'Usuario no encontrado','code':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)

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
@permission_classes([IsAuthenticated])
def actividades(request):
    """Método para obtener las actividades y crear una nueva actividad"""

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
@permission_classes([IsAuthenticated])
def actividad(request, pk):
    """Método para obtener, actualizar o eliminar una actividad"""
    

    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return Response({'data':'Actividad no encontrada','code':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)

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
@permission_classes([IsAuthenticated])
def sectores(request):
    """Método para obtener los sectores y crear un nuevo sector"""
    

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
@permission_classes([IsAuthenticated])
def sector(request, pk):
    """Método para obtener, actualizar o eliminar un sector"""
    

    try:
        sector = Sector.objects.get(pk=pk)
    except Sector.DoesNotExist:
        return Response({'data':'Sector no encontrado','code':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)

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


#Empresas
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def empresas(request):
    """Método para obtener las empresas y crear una nueva empresa"""

    if request.method == 'GET':
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_201_CREATED},status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

#Empresa
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def empresa(request, pk):
    """Método para obtener, actualizar o eliminar una empresa"""
    

    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return Response({'data':'Empresa no encontrada','code':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'code':status.HTTP_202_ACCEPTED},status.HTTP_202_ACCEPTED)
        return Response({'data':serializer.errors,'code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empresa.delete()
        return Response({'data':'Eliminación exitosa','code':status.HTTP_204_NO_CONTENT})


#Contratos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contratos(request):
    """Método para obtener los contratos y crear un nuevo contrato"""
    

    if request.method == 'GET':
        contratos = Contrato.objects.all()
        serializer = ContratosSerializer(contratos, many=True)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)

    elif request.method == 'POST':
        actividades = []
        sectores = []
        usuarios_supervisores = []
        usuarios_fiscalizadores = []

        contrato = {}
        
        print("REQUESTT",request.data)
        #Crear registros en tabla ContratoXSector
        for sector in request.data['sectores']:
            print(sector['sector_data'])
            sector_data = Sector.objects.get(pk=sector['sector_data'])
            sector_instance = ContratoXSector.objects.create(
                sector_data = sector_data,
                nombre_sector = sector['nombre_sector']
            )

            for actividad in sector['actividades']:
                actividad_data = Actividad.objects.get(pk=actividad)
                actividades.append(actividad_data)

            #Obtener data de usuarios
            for usuario in sector['usuarios_supervisores']:
                usuario_data = Usuarios.objects.get(pk=usuario)
                usuarios_supervisores.append(usuario_data)
            
            for usuario in sector['usuarios_fiscalizadores']:
                usuario_data = Usuarios.objects.get(pk=usuario)
                usuarios_fiscalizadores.append(usuario_data)


            #Setear objetos actividades
            for actividad in actividades:
                sector_instance.actividades.add(actividad)

            #Setear objetos supervisores a sector
            for usuario in usuarios_supervisores:
                sector_instance.usuarios_supervisores.add(usuario)
            
            #Setear objetos fiscalizadores a sector
            for usuario in usuarios_fiscalizadores:
                sector_instance.usuarios_fiscalizadores.add(usuario)

            sectores.append(sector_instance)

            actividades = []
            usuarios_supervisores = []
            usuarios_fiscalizadores = []

        #Crear registro en contrato
        contrato_instance = Contrato.objects.create(
            descripcion = request.data['descripcion'],
            nombre_contrato = request.data['nombre_contrato']
        )

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


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def contrato(request, pk):
    """Método para obtener y actualizar un contrato"""
    
    try:
        contrato = Contrato.objects.get(pk=pk)
    except Contrato.DoesNotExist:
        return Response({'data':'Contrato no encontrado','code':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)



    if request.method == 'GET':
        serializer = ContratosSerializer(contrato)
        return Response({'data':serializer.data,'code':status.HTTP_200_OK},status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        contratoData = ContratosSerializer(contrato).data
        #print(contratoData)

        if request.query_params.get('id_sector') == None:
            return Response({'data':'Se debe elegir un sector','code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
        
        else:

            usuarios_supervisores = []
            usuarios_fiscalizadores = []
            actividades = []

            id_sector = request.query_params.get('id_sector')
            sectorObjecto = ContratoXSector.objects.get(pk=id_sector)

            print("AAAA",sectorObjecto)


            for supervisor in request.data['sector']['usuarios_supervisores']:
                #print(supervisor)
                usuario_data = Usuarios.objects.get(pk=supervisor)
                usuarios_supervisores.append(usuario_data)


            for fiscalizador in request.data['sector']['usuarios_fiscalizadores']:
                #print(fiscalizador)
                usuario_data = Usuarios.objects.get(pk=fiscalizador)
                usuarios_fiscalizadores.append(usuario_data)


            for actividad in request.data['sector']['actividades']:
                #print(fiscalizador)
                actividad_data = Actividad.objects.get(pk=actividad)
                actividades.append(actividad_data)
            
            sectorObjecto.usuarios_supervisores.clear()
            sectorObjecto.usuarios_fiscalizadores.clear()
            sectorObjecto.actividades.clear()

            #Setear objetos supervisores a sector
            for usuario in usuarios_supervisores:
                sectorObjecto.usuarios_supervisores.add(usuario)
            
            #Setear objetos fiscalizadores a sector
            for usuario in usuarios_fiscalizadores:
                sectorObjecto.usuarios_fiscalizadores.add(usuario)

            #Setear objetos actividades a sector
            for actividad in actividades:
                sectorObjecto.actividades.add(actividad)

            serializer = ContratoXSectorSerializer(sectorObjecto, partial=True)
            
            #print("SSSSSSSSSSSSSSSS",serializer)
            return Response({'data':serializer.data,'code':status.HTTP_202_ACCEPTED},status.HTTP_202_ACCEPTED)


#Obtener contratos por usuarios
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def contratosXusuario(request):
    """Método para obtener los contratos de acuerdo al usuario"""
    

    if request.method == 'GET':


        print(request.query_params.get('tipo_usuario'))
        if request.query_params.get('tipo_usuario') == None:
            return Response({'data':'Se debe enviar un tipo de usuario','code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
        
        elif request.query_params.get('id_usuario') == None:
            return Response({'data':'Se debe enviar el id del usuario','code':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
        
        else:
            contratos = Contrato.objects.all()
            tipo_usuario = request.query_params.get('tipo_usuario')
            id_usuario = request.query_params.get('id_usuario')

            contratosRespuesta = {}
            contratosArreglo = []
            sectores = []

            serializer = []

            flag = False

            if int(tipo_usuario) == 1: #Supervisor
                for contrato in contratos:
                    serializer = ContratosSerializer(contrato)
                    dataContrato = serializer.data
                    for data in dataContrato['sectores']:
                        #print(data['usuarios_supervisores'])
                        for supervisores in data['usuarios_supervisores']:
                            if int(id_usuario) == int(supervisores['id']):
                                sectores.append(data)
                                flag = True
                    if flag:
                        print(sectores)
                        contratosRespuesta['nombre_contrato'] = serializer.data['nombre_contrato']
                        contratosRespuesta['descripcion'] = serializer.data['descripcion']
                        contratosRespuesta['id_contrato'] = serializer.data['id']
                        contratosRespuesta['contratoActivo'] = serializer.data['contratoActivo']
                        contratosRespuesta['sectores'] = sectores
                        contratosArreglo.append(contratosRespuesta)

                        contratosRespuesta = {}
                        sectores = []
                        flag = False

            if int(tipo_usuario) == 2: #Fiscalizador
                for contrato in contratos:
                    serializer = ContratosSerializer(contrato)
                    dataContrato = serializer.data
                    for data in dataContrato['sectores']:
                        #print(data['usuarios_supervisores'])
                        for fiscalizador in data['usuarios_fiscalizadores']:
                            if int(id_usuario) == int(fiscalizador['id']):
                                sectores.append(data)
                                flag = True
                    if flag:
                        print(sectores)
                        contratosRespuesta['nombre_contrato'] = serializer.data['nombre_contrato']
                        contratosRespuesta['descripcion'] = serializer.data['descripcion']
                        contratosRespuesta['id_contrato'] = serializer.data['id']
                        contratosRespuesta['contratoActivo'] = serializer.data['contratoActivo']
                        contratosRespuesta['sectores'] = sectores
                        contratosArreglo.append(contratosRespuesta)

                        contratosRespuesta = {}
                        sectores = []
                        flag = False

            if len(sectores) > 0:
                print(contratosArreglo)


            return Response({'data':contratosArreglo,'code':status.HTTP_200_OK},status.HTTP_200_OK)

