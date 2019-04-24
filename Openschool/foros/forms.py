from django import forms
from django.contrib.auth.models import User
from foros.models import Pregunta,Respuesta_Pregunta




class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = (
            'Texto_Pregunta',
        )
        labels={
        'Texto_Pregunta':'Pregunta',
        }
        widgets={
         'Texto_Pregunta':forms.TextInput(attrs={'class':'form-control'}),
        }

class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Respuesta_Pregunta
        fields = (
            'Texto_Respuesta',
        )

        labels={
        'Texto_Respuesta':'Comentar',
        }

        widgets={
         'Texto_Respuesta':forms.TextInput(attrs={'class':'form-control'}),
        }
