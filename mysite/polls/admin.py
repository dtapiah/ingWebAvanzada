# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Carrera
from .models import MallaCurricular
from .models import Asignatura
from .models import InstanciaAsignatura
from .models import Estudiante

admin.site.register(Carrera)
admin.site.register(MallaCurricular)
admin.site.register(Asignatura)
admin.site.register(InstanciaAsignatura)
admin.site.register(Estudiante)

# Register your models here.
