# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
#
from django.core.files.storage import FileSystemStorage
#impoorta la tabla pregunta
from .models import Pregunta, Carrera,Materia,Respuesta_Pregunta,Articulo
# Create your views here.
#libreria que manda errores si pasan cosas que no esperamos
#es para ser try cath
from django.http import Http404,HttpResponse
from .forms import PreguntaForm,RespuestaForm
#Creacion del formulario
import datetime
from django.utils import timezone
def index(request):
    Carreras = Carrera.objects.all()
    return render(request,'foro/index.html',{'Carreras': Carreras})


def detail(request,Carrera):
    Materias = Materia.objects.get(Carrera_id = Carrera,Nombre_Materia= 'Foro_General')

    Preguntas = Pregunta.objects.filter(Materia_id= Materias.id)
    Preguntas = Preguntas.order_by('-Fecha_Publicacion')[:5]

    return render(request,'foro/detail.html',{'Preguntas': Preguntas,'Materias': Materias})

def results(request, Preguntaid):
    Comentarios = Respuesta_Pregunta.objects.filter(Pregunta_id= Preguntaid,Comentarios__isnull=True)
    Comentarios = Comentarios.order_by('-Fecha_Publicacion')[:5]
    Preguntas= Pregunta.objects.get(pk=Preguntaid)
    Respuesta_Form = RespuestaForm()
    if request.method == 'POST':
        if  request.user.is_authenticated:
            Respuesta_Form = RespuestaForm(request.POST)
            if Respuesta_Form.is_valid():
                Preguntas = Pregunta.objects.get(id = Preguntaid)
                Respuesta = Respuesta_Form.save(commit=False)
                Respuesta.user = request.user
                Respuesta.Texto_Respuesta = request.POST['Texto_Respuesta']
                Respuesta.Pregunta = Preguntas
                Respuesta.save()
                return render(request,'foro/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'Preguntas':Preguntas,'Respuesta_Form': Respuesta_Form})
    else:
        Respuesta_Form = RespuestaForm()

    return render(request,'foro/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'Preguntas':Preguntas,'Respuesta_Form': Respuesta_Form})

def resultsH(request,Preguntaid,Comentariosid):
    Comentario = Respuesta_Pregunta.objects.filter(Pregunta_id= Preguntaid,Comentarios=Comentariosid)
    Comentario = Comentario.order_by('-Fecha_Publicacion')[:5]
    ComentarioP= Respuesta_Pregunta.objects.get(pk=Comentariosid)
    Respuesta_Form = RespuestaForm()
    if request.method == 'POST':
        if  request.user.is_authenticated:
            Respuesta_Form = RespuestaForm(request.POST)
            if Respuesta_Form.is_valid():
                Preguntas = Pregunta.objects.get(id = Preguntaid)
                Respuesta = Respuesta_Form.save(commit=False)
                Respuesta.user = request.user
                Respuesta.Comentarios = ComentarioP
                Respuesta.Texto_Respuesta = request.POST['Texto_Respuesta']
                Respuesta.Pregunta = Preguntas
                Respuesta.save()
                return render(request,'foro/Comentarios.html',{'Comentarios': Comentario,'Preguntaid':Preguntaid,'ComentarioP':ComentarioP,'Respuesta_Form': Respuesta_Form})
    return render(request,'foro/Comentarios.html',{'Comentarios': Comentario,'Preguntaid':Preguntaid,'ComentarioP':ComentarioP,'Respuesta_Form': Respuesta_Form})

from .models import Pregunta, Carrera,Materia,Respuesta_Pregunta

def PreguntaFormA(request,Materiaid):
    Preguntas = Pregunta.objects.filter(Materia_id= Materiaid)
    Preguntas = Preguntas.order_by('-Fecha_Publicacion')[:5]
    if not request.user.is_authenticated:
        return render(request, 'cuentas/login.html')
    if request.method == 'POST':
        Pregunta_Form = PreguntaForm(request.POST)
        if Pregunta_Form.is_valid():
            Materias = Materia.objects.get(id = Materiaid)
            Preguntad = Pregunta_Form.save(commit=False)
            Preguntad.user = request.user
            Preguntad.Texto_Pregunta = request.POST['Texto_Pregunta']
            Preguntad.Materia = Materias
            Preguntad.save()
            return render(request,'foro/detail.html',{'Preguntas': Preguntas,'Materias': Materias})
    else:
        Pregunta_Form = PreguntaForm()
        args = {'Pregunta_Form': Pregunta_Form}
    return render(request,'foro/FormPregunta.html',args)

def Buscar(request):
    buscar=request.POST['buscalo']
    Preguntas=Pregunta.objects.filter(Texto_Pregunta__contains=buscar)
    if Preguntas:
        return render (request,'cuentas/buscar.html',{'Preguntas':Preguntas})
    else:
        Articulos=Articulo.objects.filter(Titulo__contains=buscar)
        return render (request,'cuentas/buscar.html',{'Articulos':Articulos})
