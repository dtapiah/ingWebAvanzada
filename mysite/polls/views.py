from django.http import HttpResponse
from django.template import loader
from .models import Carrera

def index(request):
	carreras = Carrera.objects.all()
	template = loader.get_template('polls/index.html')
	context = {'carreras': carreras,}
	return HttpResponse(template.render(context, request))

def carrera(request, carrera_id):
	template = loader.get_template('polls/carrera.html')
	a = Carrera.objects.get(id__exact=carrera_id)
	nombre = a.nombreCarrera
	context = {'nombre': nombre,}
	return HttpResponse(template.render(context, request))
