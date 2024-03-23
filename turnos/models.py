from django.db import models

# Create your models here.

class CategoriaTurno(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.TextField(max_length=5000, null=False)  
    icon = models.TextField(max_length=5000, null=False)
    def __str__(self):
        return self.nombre


class Asesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=5000, null=False)
    ventanilla = models.TextField(max_length=5000, null=False)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.TextField(max_length=5000, null=False)
    nombre =  models.TextField(max_length=1000, null=False)
    def __str__(self):
        return self.nombre


  
class EstadoTurno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, null=False)
    def __str__(self):
        return self.nombre
    

class Turno(models.Model):
    id = models.AutoField(primary_key=True) 
    consecutivo = models.TextField(max_length=5000, null=False)
    id_categoria =  models.ForeignKey('CategoriaTurno', on_delete=models.SET_NULL, null=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    fecha_hora_solicitud = models.DateTimeField(null=True)
    id_asesor = models.IntegerField 
    id_estado_turno = models.ForeignKey('EstadoTurno', on_delete=models.SET_NULL, null=True)
    fecha_hora_atencion_turno = models.DateTimeField(null=True)
    fecha_hora_finalizacion_turno = models.DateTimeField(null=True)
    def __str__(self):
        return self.consecutivo

  
    






