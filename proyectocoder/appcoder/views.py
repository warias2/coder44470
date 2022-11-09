from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.models import Profesor
from django.shortcuts import render
from appcoder.form import CursoFormulario
from appcoder.form import ProfesorFormulario

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    # Obtenes el listado de objetos en la BD
    cursos = Curso.objects.all()

    for curso in cursos:
        print(curso.nombre)

    return render(request, "appcoder/cursos.html")
    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")

def curso_formulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, "appcoder/index.html")
    else:
        miFormulario = CursoFormulario()
    
    return render(request, "appcoder/curso_formulario.html", {"miFormulario":miFormulario})

def profesor_formulario(request):
    
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "appcoder/index.html")
    else:
        miFormulario = ProfesorFormulario()
    
    return render(request, "appcoder/profesor_formulario.html", {"miFormulario":miFormulario})

def busqueda_camada(request):

    return render(request, "appcoder/busqueda_camada.html")

def buscar(request):
    
    if request.GET['camada']:
        camada = request.GET['camada']
        nombre = Curso.objects.filter(camada__icontains=camada)
        return render(request, "appcoder/resultados_busqueda.html", {"nombre":nombre, "camada":camada})
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     # Respuesta casera
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
#     cadena_respuesta += "</ul>"

#     return HttpResponse(cadena_respuesta)