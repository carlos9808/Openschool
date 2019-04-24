from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
#
from django.core.files.storage import FileSystemStorage
#impoorta la tabla pregunta
from foros.models import  Carrera,Materia,Articulo,Comentario_Articulo
# Create your views here.
#libreria que manda errores si pasan cosas que no esperamos
#es para ser try cath
from django.http import Http404,HttpResponse
#Creacion del formulario
import datetime
from django.utils import timezone
from .forms import ArticuloForm,RespuestaFormA
from foros.forms import PreguntaForm


def index(request):
    Carreras = Carrera.objects.all()
    return render(request,'articulos/index.html',{'Carreras': Carreras})

def detail(request,Carrera):
    Materias = Materia.objects.get(Carrera_id = Carrera,Nombre_Materia= 'Foro_General')

    Articulos = Articulo.objects.filter(Materia_id= Materias.id)
    Articulos = Articulos.order_by('-Fecha_Publicacion')[:5]

    return render(request,'articulos/detail.html',{'Articulos': Articulos,'Materias': Materias})

def results(request, Preguntaid):
    Comentarios = Comentario_Articulo.objects.filter(Articulo_id= Preguntaid,Comentarios__isnull=True)
    Comentarios = Comentarios.order_by('-Fecha_Publicacion')[:5]
    Articulos= Articulo.objects.get(pk=Preguntaid)
    Respuesta_Form = RespuestaFormA()
    if request.method == 'POST':
        if  request.user.is_authenticated:
            Respuesta_Form = RespuestaFormA(request.POST)
            if Respuesta_Form.is_valid():
                Articulos = Articulo.objects.get(id = Preguntaid)
                Respuesta = Respuesta_Form.save(commit=False)
                Respuesta.user = request.user
                Respuesta.Texto_Respuesta = request.POST['Texto_Respuesta']
                Respuesta.Articulo = Articulos
                Respuesta.save()
                return render(request,'articulos/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'Articulos':Articulos,'Respuesta_Form': Respuesta_Form})
    else:
        Respuesta_Form = RespuestaFormA()

    return render(request,'articulos/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'Articulos':Articulos,'Respuesta_Form': Respuesta_Form})

def resultsH(request,Preguntaid,Comentariosid):
    Comentarios = Comentario_Articulo.objects.filter(Articulo_id= Preguntaid,Comentarios=Comentariosid)
    Comentarios = Comentarios.order_by('-Fecha_Publicacion')[:5]
    ComentarioP= Comentario_Articulo.objects.get(pk=Comentariosid)
    Respuesta_Form = RespuestaFormA()
    if request.method == 'POST':
        if  request.user.is_authenticated:
            Respuesta_Form = RespuestaFormA(request.POST)
            if Respuesta_Form.is_valid():
                Articulos = Articulo.objects.get(id = Preguntaid)
                Respuesta = Respuesta_Form.save(commit=False)
                Respuesta.user = request.user
                Respuesta.Comentarios = ComentarioP
                Respuesta.Texto_Respuesta = request.POST['Texto_Respuesta']
                Respuesta.Articulo = Articulos
                Respuesta.save()
                return render(request,'articulos/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'ComentarioP':ComentarioP,'Respuesta_Form': Respuesta_Form})
    return render(request,'articulos/Comentarios.html',{'Comentarios': Comentarios,'Preguntaid':Preguntaid,'ComentarioP':ComentarioP,'Respuesta_Form': Respuesta_Form})


def ArticuloFormA(request,Materiaid):
    Articulos = Articulo.objects.filter(Materia_id= Materiaid)
    Articulos = Articulos.order_by('-Fecha_Publicacion')[:5]
    Pregunta_Form = ArticuloForm()
    args = {'Pregunta_Form': Pregunta_Form}
    if request.method == 'POST':
        form = ArticuloForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            Materias = Materia.objects.get(id = Materiaid)
            Preguntad = form.save(commit=False)
            Preguntad.user = request.user
            Preguntad.Texto_Pregunta = request.POST['Titulo']
            Preguntad.Materia = Materias
            Preguntad.Pdf_articulo = request.FILES['Pdf_articulo']
            Preguntad.save()
            Articulos = Articulo.objects.filter(Materia_id= Materiaid)
            Articulos = Articulos.order_by('-Fecha_Publicacion')[:5]
            return render(request,'articulos/detail.html',{'Articulos': Articulos,'Materias': Materias})
    else:
        Pregunta_Form = ArticuloForm()
        args = {'Pregunta_Form': Pregunta_Form}
    return render(request,'articulos/ArticulosForm.html',args)
