from rest_framework import serializers 
from turnos.models import CategoriaTurno , Asesor , Usuario , EstadoTurno, Turno



class CategoriaTurnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaTurno
        exclude = []

class AsesorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asesor
        exclude = []

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = []


class EstadoTurnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoTurno
        exclude = []



class TurnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Turno
        exclude = []

class TurnoUserSerializers(serializers.ModelSerializer):

    nombre_usuario = serializers.CharField(source='id_usuario.nombre', read_only=True)
    documento_usuario = serializers.CharField(source='id_usuario.documento', read_only=True)


    class Meta:
        model = Turno
        fields = ['id', 'consecutivo',  'nombre_usuario' , 'documento_usuario'] 

