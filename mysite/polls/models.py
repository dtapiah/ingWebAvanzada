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