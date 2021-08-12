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
   path('actividades/', views.actividades),
   path('actividades/<int:pk>', views.actividad),
   path('sectores/', views.sectores),
   path('sectores/<int:pk>', views.sector),
   path('contratos/', views.contratos),
   #path('',include(router.urls))
]