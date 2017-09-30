from django.contrib import admin
from .models import Estudiante
from .models import Inscripcion_Asignatura
from .models import Carrera
from .models import MallaCurricular
from .models import Asignatura
from .models import InstanciaAsignatura
from .models import Profesor
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Inscripcion_Asignatura)
admin.site.register(Carrera)
admin.site.register(MallaCurricular)
admin.site.register(Asignatura)
admin.site.register(InstanciaAsignatura)
admin.site.register(Profesor)