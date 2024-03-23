from django.shortcuts import render
from .serializers import CategoriaTurnoSerializers , AsesorSerializers, TurnoUserSerializers, UsuarioSerializers, EstadoTurnoSerializers, TurnoSerializers
from rest_framework import viewsets
from datetime import timedelta

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CategoriaTurno  , Asesor, Usuario, EstadoTurno, Turno

from rest_framework import status
from django.http import Http404

# Create your views here.

class CategeoriaTurno_APIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                categoria = CategoriaTurno.objects.get(pk=pk)
            except CategoriaTurno.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = CategoriaTurnoSerializers(categoria)
            return Response(serializer.data)
        else:
            # Si no se proporciona un pk, devolvemos todas las instancias
            categorias = CategoriaTurno.objects.all()
            serializer = CategoriaTurnoSerializers(categorias, many=True)
        return Response(serializer.data)

class Asesor_APIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                asesor = Asesor.objects.get(pk=pk)
            except Asesor.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = AsesorSerializers(asesor)
            return Response(serializer.data)
        else:
            asesor = Asesor.objects.all()
            serializer = AsesorSerializers(asesor, many=True)
        return Response(serializer.data)
    
class Usuario_APIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                usuario = Usuario.objects.get(pk=pk)
            except Usuario.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UsuarioSerializers(usuario)
            return Response(serializer.data)
        else:
            usuario = Usuario.objects.all()
            serializer = UsuarioSerializers(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstadoTurno_APIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                estadoturno = EstadoTurno.objects.get(pk=pk)
            except EstadoTurno.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EstadoTurnoSerializers(estadoturno)
            return Response(serializer.data)
        else:
            estadoturnos = EstadoTurno.objects.all()
            serializer = EstadoTurnoSerializers(estadoturnos, many=True)
        return Response(serializer.data)
    
class Turno_APIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                turno = Turno.objects.get(pk=pk)
            except Turno.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TurnoSerializers(turno)
            return Response(serializer.data)
        else:
            turno = Turno.objects.all()
            serializer = TurnoSerializers(turno, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        # Obtener los datos del request
        categoria_id = request.data.get('id_categoria')
        id_usuario = request.data.get('id_usuario')
        id_estado_turno = 1

        # Consultar la categoría
        categoria_turno = CategoriaTurno.objects.filter(id=categoria_id).first()

        # Obtener la fecha actual
        fecha_actual = timezone.now().date()

        # Obtener todos los turnos para la categoría en el día actual
        turnos_hoy = Turno.objects.filter(id_categoria=categoria_id, fecha_hora_atencion_turno__date=fecha_actual).order_by('-id')
        
        for turno in turnos_hoy:
            print(turno.id)  # Por ejemplo, imprimir el ID del turno
            print(turno.consecutivo)

        # Si hay turnos hoy, tomar el último y aumentar su consecutivo
        if turnos_hoy.exists():
            ultimo_turno_hoy = turnos_hoy.first()
            ultimo_numero = int(ultimo_turno_hoy.consecutivo[1:])
            nuevo_numero = ultimo_numero + 1
            nuevo_consecutivo = f"{categoria_turno.nombre[0]}{nuevo_numero}"
        else:
            # Si no hay turnos para esa categoría en el día actual, comenzar desde 1
            nuevo_consecutivo = f"{categoria_turno.nombre[0]}1"

        fecha_hora_atencion_turno = timezone.now()

        # Crear un nuevo diccionario con los datos necesarios
        data = {
            'id_categoria': categoria_id,
            'id_usuario': id_usuario,
            'consecutivo': nuevo_consecutivo,
            'fecha_hora_atencion_turno': fecha_hora_atencion_turno,
            'id_estado_turno' : id_estado_turno
        }

        # Serializar los datos
        serializer = TurnoSerializers(data=data)

        # Validar y guardar el objeto
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Turnos_APIView(APIView):
    def get(self, request, pk=None, format=None):
        fecha_actual = timezone.now().date()  # Obtiene la fecha actual sin la parte de tiempo

        if pk is not None:
            try:
                turno = Turno.objects.get(fecha_hora_atencion_turno__date=fecha_actual, id=pk)
            except Turno.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TurnoSerializers(turno)
            return Response(serializer.data)
        else:
            # Obtiene la fecha actual sin la parte de tiempo
            fecha_actual = timezone.now().date()

            # Filtra los turnos para aquellos cuya fecha_hora_atencion_turno tenga la misma fecha que la fecha actual
            turnos = Turno.objects.filter(
                fecha_hora_atencion_turno__date=fecha_actual,
                id_estado_turno=1
            ).select_related('id_usuario')  # Realiza el join con la tabla Usuario

            serializer = TurnoUserSerializers(turnos, many=True)
            return Response(serializer.data)