from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Estudiante
from .models import Profesor
from .models import Inscripcion_Asignatura
from .models import InstanciaAsignatura
from .models import Asignatura
from .models import Carrera
from .models import MallaCurricular



class Inscipciones:
	def __init__(self):
		self.carrera = ''
		self.clave = ''
		self.nombre = ''
		self.anno = ''
		self.semestre = ''
		self.estado = ''



class Asinaturas:
	def __init__(self):
		self.carrera = ''
		self.clave = ''
		self.nombre = ''
		self.anno = ''
		self.semestre = ''


		
def index(request):
    template = loader.get_template('navegadorcito/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))



	
def guardar_estudiante(request):	
	obj_estudiante = Estudiante.objects.get(dni=request.POST['dni'])
	obj_estudiante.fono=request.POST['fono']
	obj_estudiante.direccion=request.POST['direccion']
	obj_estudiante.correo=request.POST['correo']
	obj_estudiante.save()
	lista_inscipciones = []
	
	var_carrera = ''
	var_anno = '2017' 
	var_semestre = '2' 
	var_estado = '' 		
	obj_estudiante = Estudiante.objects.get(dni=request.POST['dni'])
	lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
	for obj in lista:
		ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
		asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id)
		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id)
		carrera= Carrera.objects.get(id=malla.carrera.id)
		inscripcion = Inscipciones()
		
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = ins_asig.anno
		inscripcion.semestre = ins_asig.semestre
		inscripcion.estado = obj.estado
		#filtro
		if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.anno == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
			lista_inscipciones.append(inscripcion)
	
	context = {
		'usuario': obj_estudiante,
		'lista_inscipciones': lista_inscipciones,
		'carrera' : var_carrera,
		'anno' : var_anno,
		'semestre' : var_semestre,
		'estado' : var_estado
	}
	return render(request, 'navegadorcito/estudiante.html', context)



	
def editar_estudiante(request):
	estudiante = Estudiante.objects.get(dni=request.POST['dni'])
	context = {
        'usuario': estudiante
	}
	return render(request, 'navegadorcito/editar_estudiante.html', context)




def ingreso_login(request):
	lista_inscipciones = []
	lista_asinaturas = []
	variableI = []
	estu = []
	
	if(request.POST['tipo'] == 'E'):
		try:
			vista = True
			usuarioE = Estudiante.objects.get(dni=request.POST['dni'],password=request.POST['password'])
			var_carrera = ''
			var_anno = '' 
			var_semestre = '' 
			var_estado = '' 		
			obj_estudiante = Estudiante.objects.get(dni=request.POST['dni'])
			lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
			for obj in lista:
				ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
				asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id) 
				malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id) 
				carrera= Carrera.objects.get(id=malla.carrera.id) 
				
				inscripcion = Inscipciones()
				inscripcion.carrera = carrera.nombreCarrera
				inscripcion.clave = asignatura.claveAsignatura
				inscripcion.nombre = asignatura.nombreAsignatura
				inscripcion.anno = ins_asig.anno
				inscripcion.semestre = ins_asig.semestre
				inscripcion.estado = obj.estado
				#filtro
				if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.carrera == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
					lista_inscipciones.append(inscripcion)
			
			context = {
				'usuario': obj_estudiante,
				'lista_inscipciones': lista_inscipciones,
				'carrera' : var_carrera,
				'anno' : var_anno,
				'vista': vista,
				'semestre' : var_semestre,
				'estado' : var_estado
			}
			return render(request, 'navegadorcito/estudiante.html', context)
		except:
			return render(request, 'navegadorcito/error.html')
	
	if(request.POST['tipo'] == 'P'):
		try:
			Profesor.objects.get(dniP=request.POST['dni'],passwordP=request.POST['password'])
			usuarioP = Profesor.objects.get(dniP=request.POST['dni'],passwordP=request.POST['password'])
			var_carrera = ''
			var_anno = '' 
			var_semestre = ''
			var_estado = ''
			var_carrerap = ''
			var_annop = '' 
			var_semestrep = '' 
			obj_profe = Profesor.objects.get(dniP=request.POST['dni'])

			lista = InstanciaAsignatura.objects.filter(profe=obj_profe.id)
			for obj in lista:
				asignatura = Asignatura.objects.get(id=obj.asignatura.id)
				
				ins = Inscripcion_Asignatura.objects.get(id=obj.id)
		
				variableI.append(ins.estudiante_id)

				malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id)
				carrera= Carrera.objects.get(id=malla.carrera.id)

				inscripcion = Asinaturas()
				inscripcion.carrera = carrera.nombreCarrera
				inscripcion.clave = asignatura.claveAsignatura
				inscripcion.nombre = asignatura.nombreAsignatura
				inscripcion.anno = obj.anno
				inscripcion.semestre = obj.semestre
				inscripcion.estudiante = ins.estudiante_id			
				
				#filtro
				if((inscripcion.anno == var_annop or var_annop == '') and (inscripcion.carrera == var_carrerap or var_carrerap == '') and (inscripcion.semestre == var_semestrep or var_semestrep == '')):
					lista_asinaturas.append(inscripcion)

			listaI = []
			for i in variableI:
				if i not in listaI:
					listaI.append(i)
					estu.append(Estudiante.objects.get(id=i))

			context2 = {
				'usuario': obj_profe,
				'lista_asinaturas': lista_asinaturas,
				'listaI': listaI,
				'estu': estu,
				'carrera' : var_carrerap,
				'anno' : var_annop,
				'semestre' : var_semestrep
			}
			return render(request, 'navegadorcito/profesor.html', context2)
		except:
			return render(request, 'navegadorcito/error.html')



def ficha(request, i):
	vista = False
	lista_inscipciones = []
	obj_estudiante= Estudiante.objects.get(id=i)
	usuarioE = Estudiante.objects.get(dni=obj_estudiante.dni,password=obj_estudiante.password)
	var_carrera = ''
	var_anno = '' 
	var_semestre = '' 
	var_estado = '' 		
	lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
	for obj in lista:
		ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
		asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id) 
		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id) 
		carrera= Carrera.objects.get(id=malla.carrera.id) 
		
		inscripcion = Inscipciones()
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = ins_asig.anno
		inscripcion.semestre = ins_asig.semestre
		inscripcion.estado = obj.estado
		#filtro
		if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.carrera == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
			lista_inscipciones.append(inscripcion)
	
	context = {
		'usuario': obj_estudiante,
		'vista': vista,
		'lista_inscipciones': lista_inscipciones,
		'carrera' : var_carrera,
		'anno' : var_anno,
		'semestre' : var_semestre,
		'estado' : var_estado
	}
	return render(request, 'navegadorcito/estudiante.html', context)


def recargar_profe(request):
	usuarioP = Profesor.objects.get(dniP=request.POST['dni'])
	lista_asinaturas = []

	var_carrerap = request.POST['carrera']
	var_annop = request.POST['anno']
	var_semestrep = request.POST['semestre']  
	obj_profe = Profesor.objects.get(dniP=request.POST['dni'])

	lista = InstanciaAsignatura.objects.filter(profe=obj_profe.id)
	for obj in lista:
		asignatura = Asignatura.objects.get(id=obj.asignatura.id)
		
		ins = Inscripcion_Asignatura.objects.get(id=obj.id)

		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id)
		carrera= Carrera.objects.get(id=malla.carrera.id)

		inscripcion = Asinaturas()
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = obj.anno
		inscripcion.semestre = obj.semestre
		inscripcion.estudiante = ins.estudiante_id		
		
		#filtro
		if((inscripcion.anno == var_annop or var_annop == '') and (inscripcion.carrera == var_carrerap or var_carrerap == '') and (inscripcion.semestre == var_semestrep or var_semestrep == '')):
			lista_asinaturas.append(inscripcion)

	context2 = {
		'usuario': obj_profe,
		'lista_asinaturas': lista_asinaturas,
		'carrera' : var_carrerap,
		'anno' : var_annop,
		'semestre' : var_semestrep
	}
	return render(request, 'navegadorcito/profesor.html', context2)


def filtro(request, j):
	lista_asinaturas = []
	variableI = []
	estu = []
	var_carrera = ''
	var_anno = '' 
	var_semestre = ''
	var_estado = ''
	var_carrerap = ''
	var_annop = '' 
	var_semestrep = '' 
	obj_profe = Profesor.objects.get(dniP=j)

	lista = InstanciaAsignatura.objects.filter(profe=obj_profe.id)
	for obj in lista:
		asignatura = Asignatura.objects.get(id=obj.asignatura.id)
		
		ins = Inscripcion_Asignatura.objects.get(id=obj.id)

		variableI.append(ins.estudiante_id)

		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id)
		carrera= Carrera.objects.get(id=malla.carrera.id)

		inscripcion = Asinaturas()
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = obj.anno
		inscripcion.semestre = obj.semestre
		inscripcion.estudiante = ins.estudiante_id			
		
		#filtro
		if((inscripcion.anno == var_annop or var_annop == '') and (inscripcion.carrera == var_carrerap or var_carrerap == '') and (inscripcion.semestre == var_semestrep or var_semestrep == '')):
			lista_asinaturas.append(inscripcion)

	listaI = []
	for i in variableI:
		if i not in listaI:
			listaI.append(i)
			estu.append(Estudiante.objects.get(id=i))

	context2 = {
		'usuario': obj_profe,
		'lista_asinaturas': lista_asinaturas,
		'listaI': listaI,
		'estu': estu,
		'carrera' : var_carrerap,
		'anno' : var_annop,
		'semestre' : var_semestrep
	}
	return render(request, 'navegadorcito/filtro_estudiantes.html', context2)


	
def recargar_estudiante(request):
	usuario = Estudiante.objects.get(dni=request.POST['dni'])
	lista_inscipciones = []

	var_nombreE = request.POST['nombre']
	var_apellidoE = request.POST['apellido']
	var_carrera = request.POST['carrera']
	var_anno = request.POST['anno']
	var_semestre = request.POST['semestre'] 
	var_estado = request.POST['estado'] 
	obj_estudiante = Estudiante.objects.get(dni=request.POST['dni'])

	lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
	for obj in lista:
		ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
		asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id)
		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id)
		carrera= Carrera.objects.get(id=malla.carrera.id)
		inscripcion = Inscipciones()
		
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = ins_asig.anno
		inscripcion.semestre = ins_asig.semestre
		inscripcion.estado = obj.estado
		#filtro
		if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.carrera == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
			lista_inscipciones.append(inscripcion)
	
	context = {
		'usuario': obj_estudiante,
		'lista_inscipciones': lista_inscipciones,
		'carrera' : var_carrera,
		'anno' : var_anno,
		'semestre' : var_semestre,
		'estado' : var_estado,
		'nombre': var_nombreE,
		'apellido': var_apellidoE
	}	
	return render(request, 'navegadorcito/estudiante.html', context)



def recargar_estudianteP(request, j):
	usuario = Estudiante.objects.get(id=j)
	lista_inscipciones = []

	var_carrera = ''
	var_anno = '' 
	var_semestre = '' 
	var_estado = '' 		
	obj_estudiante = Estudiante.objects.get(id=j)
	lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
	for obj in lista:
		ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
		asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id) 
		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id) 
		carrera= Carrera.objects.get(id=malla.carrera.id) 
		
		inscripcion = Inscipciones()
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = ins_asig.anno
		inscripcion.semestre = ins_asig.semestre
		inscripcion.estado = obj.estado
		#filtro
		if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.carrera == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
			lista_inscipciones.append(inscripcion)
	
	context = {
		'usuario': obj_estudiante,
		'lista_inscipciones': lista_inscipciones,
		'carrera' : var_carrera,
		'anno' : var_anno,
		'semestre' : var_semestre,
		'estado' : var_estado
	}
	return render(request, 'navegadorcito/estudiante.html', context)



def recargar_estudiante2(request):
	if request.POST['nombre'] and request.POST['apellido']:
		if request.POST['nombre'] == request.POST['apellido']:
			a = (request.POST['nombre'])
		else:
			return render(request, 'navegadorcito/error_con.html')

	elif request.POST['nombre']:
		a = (request.POST['nombre'])

	elif request.POST['apellido']:
		a = (request.POST['apellido'])

	usuario = Estudiante.objects.get(dni=a)
	lista_inscipciones = []

	var_carrera = ''
	var_anno = '' 
	var_semestre = '' 
	var_estado = '' 		
	obj_estudiante = Estudiante.objects.get(dni=a)
	lista = Inscripcion_Asignatura.objects.filter(estudiante=obj_estudiante.id)
	for obj in lista:
		ins_asig = InstanciaAsignatura.objects.get(id=obj.asignatura.id)
		asignatura = Asignatura.objects.get(id=ins_asig.asignatura.id) 
		malla= MallaCurricular.objects.get(id=asignatura.mallaCurricular.id) 
		carrera= Carrera.objects.get(id=malla.carrera.id) 
		
		inscripcion = Inscipciones()
		inscripcion.carrera = carrera.nombreCarrera
		inscripcion.clave = asignatura.claveAsignatura
		inscripcion.nombre = asignatura.nombreAsignatura
		inscripcion.anno = ins_asig.anno
		inscripcion.semestre = ins_asig.semestre
		inscripcion.estado = obj.estado
		#filtro
		if((inscripcion.anno == var_anno or var_anno == '') and (inscripcion.carrera == var_carrera or var_carrera == '') and (inscripcion.semestre == var_semestre or var_semestre == '') and (inscripcion.estado == var_estado or var_estado == '')):
			lista_inscipciones.append(inscripcion)
	
	context = {
		'usuario': obj_estudiante,
		'lista_inscipciones': lista_inscipciones,
		'carrera' : var_carrera,
		'anno' : var_anno,
		'semestre' : var_semestre,
		'estado' : var_estado
	}
	return render(request, 'navegadorcito/estudiante.html', context)