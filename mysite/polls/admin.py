# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Carrera
from .models import MallaCurricular

admin.site.register(Carrera)
admin.site.register(MallaCurricular)

# Register your models here.
