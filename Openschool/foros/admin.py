from django.contrib import admin

# Register your models here.
from .models import Pregunta, Articulo,Carrera,Inscripcion,Materia,Respuesta_Pregunta
admin.site.register(Pregunta)
admin.site.register(Articulo)
admin.site.register(Carrera)
admin.site.register(Inscripcion)
admin.site.register(Materia)
admin.site.register(Respuesta_Pregunta)
