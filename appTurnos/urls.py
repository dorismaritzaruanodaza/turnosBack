"""
URL configuration for appTurnos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from turnos.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoria-turno/<int:pk>', CategeoriaTurno_APIView.as_view()),
    path('categoria-turno/', CategeoriaTurno_APIView.as_view()),
    path('asesor/' , Asesor_APIView.as_view()),
    path('asesor/<int:pk>' , Asesor_APIView.as_view()),
    path('usuario/' , Usuario_APIView.as_view()),
    path('usuario/<int:pk>' , Usuario_APIView.as_view()),
    path('estado-turno/' , EstadoTurno_APIView.as_view()),
    path('estado-turno/<int:pk>' , EstadoTurno_APIView.as_view()),
    path('turnos/' , Turno_APIView.as_view()),
    path('turnos/<int:pk>' , Turno_APIView.as_view()),
    path('getTurnos/' , Turnos_APIView.as_view())

]
