from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("profesores/", profesores, name="coder-profesores"),
    path("cursos/", cursos, name="coder-cursos"),
    path("entregables/", entregables, name="coder-entregables"),
    path("curso_formulario/", curso_formulario, name ="curso-formulario"),
    path("profesor_formulario/", profesor_formulario, name="profesor-formulario"),
    path("busqueda_camada/", busqueda_camada, name="busqueda-camada"),
    path("buscar/", buscar, name="buscar"),
]