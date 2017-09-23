import datetime

from django.db import models
from django.utils import timezone

class Carrera(models.Model):
    nombreCarrera = models.CharField(max_length=250)
    sigla = models.CharField(max_length=20)
    universidad = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreCarrera + ' - ' + self.sigla

class MallaCurricular(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombreMalla = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreMalla

class Asignatura(models.Model):
    mallaCurricular = models.ForeignKey(MallaCurricular, on_delete=models.CASCADE)
    nombreAsignatura = models.CharField(max_length=250)
    claveAsignatura = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreAsignatura

class InstanciaAsignatura(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    anno = models.CharField(max_length=20)
    semestre = models.CharField(max_length=20)

    def __str__(self):
        return self.anno

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    fono = models.CharField(max_length=20,null=True)
    direccion = models.CharField(max_length=50,null=True)
    correo = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nombre