from django import forms
from cuentas.models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from foros.models import Inscripcion

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text="",)
    password2 = forms.CharField(
        label=("Confirma contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text="",)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
        labels = {
        'username': 'Usuario',
        'first_name':'Nombre',
        'last_name':'Apellido',

        }
        help_text={
        'password1':"",
        'password2':"",
        }
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),

        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


        return user

class Datos(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ['edad','perfil']

        labels={'edad':'Edad'}

        widgets={'edad':forms.TextInput(attrs={'class':'form-control'})}
