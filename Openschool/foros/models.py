from django.db import models

import datetime
from django.utils import timezone
from cuentas.models import Usuarios
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
class Carrera(models.Model):
    Nombre_Carrera = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_Carrera
@receiver(post_save, sender=Carrera)
def save_Carrera(sender, instance, **kwargs):
    if kwargs['created']:
        Materia.objects.create(Carrera=instance,Nombre_Materia='Foro_General')


class Materia(models.Model):
    Nombre_Materia = models.CharField(max_length=200)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre_Materia

class Inscripcion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)


class Pregunta(models.Model):
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Texto_Pregunta = models.CharField(max_length=200)
    Fecha_Publicacion = models.DateTimeField('date published',auto_now=True)
    Estado = models.BooleanField(default=False)
    def was_published_recently(self):
        return self.Fecha_Publicacion >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self):
        return self.Texto_Pregunta



class Articulo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE,default=1)
    Pdf_articulo = models.FileField()
    Fecha_Publicacion = models.DateTimeField('date published',auto_now=True)
    Titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.Titulo

class Respuesta_Pregunta(models.Model):
    Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    Texto_Respuesta = models.CharField(max_length=200)
    Comentarios = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank =True)
    Fecha_Publicacion = models.DateTimeField('date published',auto_now=True)
    def __str__(self):
        return self.Texto_Respuesta


class Comentario_Articulo(models.Model):
    Articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    Texto_Respuesta = models.CharField(max_length=200)
    Comentarios = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank =True)
    Fecha_Publicacion = models.DateTimeField('date published',auto_now=True)
    def __str__(self):
        return self.Texto_Respuesta
