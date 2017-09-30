from django.conf.urls import url

from . import views
app_name = 'navegadorcito3'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('editar_estudiante/', views.editar_estudiante, name='editar_estudiante'),
	url('guardar_estudiante/', views.guardar_estudiante, name='estudiante'),
	url('ingreso_login/', views.ingreso_login, name='perfil'),
	url('recargar_estudiante/', views.recargar_estudiante, name='perfil'),
	url('recargar_profe/', views.recargar_profe, name='perfil'),
	url(r'^(?P<j>[0-9]+)/$', views.filtro, name='filtro'),
	url(r'^(?P<i>[0-9]+)/$', views.ficha, name='ficha'),
	url(r'^profe/(?P<j>[0-9]+)/$', views.recargar_estudianteP, name='recargar_estudianteP'),
	url('recargar_estudiante2/', views.recargar_estudiante2, name='recargar_estudiante2'),

]