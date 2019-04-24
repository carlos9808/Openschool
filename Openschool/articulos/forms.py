
from django import forms
from django.contrib.auth.models import User
from foros.models import Articulo,Comentario_Articulo






class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = (
            'Titulo','Pdf_articulo',
        )

        labels={
        'Titulo':'Título',
        }

        widgets={
         'Titulo':forms.TextInput(attrs={'class':'form-control'}),
        }





class RespuestaFormA(forms.ModelForm):

    class Meta:
        model = Comentario_Articulo
        fields = (
            'Texto_Respuesta',
        )

        labels={
        'Texto_Respuesta':'Comentar',
        }

        widgets={
         'Texto_Respuesta':forms.TextInput(attrs={'class':'form-control'}),
        }
