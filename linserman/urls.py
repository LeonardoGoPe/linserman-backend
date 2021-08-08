# Use include() to add paths from the linserman
from .views import *
from linserman import views
from django.urls import path, include
from rest_framework import routers

route = routers.SimpleRouter()
route.register("usuarios",UsuariosViewSet)

urlpatterns = route.urls

urlpatterns += path('login',views.login),