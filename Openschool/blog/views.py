from django.shortcuts import render
from foros.models import Pregunta
from cuentas.models import Usuarios
from django.contrib.auth.models import User
# Create your views here.
def blogs(request):
    Pregunta_Usuario = Pregunta.objects.filter(user=request.user)
    Pregunta_Usuario = Pregunta_Usuario.order_by('-Fecha_Publicacion')[:5]
    Usuario=Usuarios.objects.get(user=request.user)
    return render(request,'blog/blog.html',{'Pregunta_Usuario':Pregunta_Usuario, 'Usuario':Usuario})

