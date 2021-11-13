# Use include() to add paths from the linserman
from django.db import router
from .views import *
from linserman import views
from django.urls import path, include
from rest_framework import routers

#router = routers.DefaultRouter()

#router.register('usuarios',views.UsuariosViewSet)

urlpatterns = [
   path('login',views.login),
   path('usuarios/', views.usuarios),
   path('usuarios/<int:pk>', views.usuario),
   path('usuarios/cambiopass/<int:pk>', views.cambioPassword),
   path('actividades/', views.actividades),
   path('actividades/<int:pk>', views.actividad),
   path('sectores/', views.sectores),
   path('sectores/<int:pk>', views.sector),
   path('contratos/', views.contratos),
   path('contratos/<int:pk>', views.contrato),
   path('contratoCabecera/<int:pk>', views.contratoCabecera),
   path('contratoAgregarSector/<int:pk>', views.contratoAgregarSector),
   path('empresas/', views.empresas),
   path('empresas/<int:pk>', views.empresa),
   path('obtener_contratos/', views.contratosXusuario),
   #path('',include(router.urls))
]