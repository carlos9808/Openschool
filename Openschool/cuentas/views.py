from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserForm, Datos
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.urls import reverse
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'cuentas/index.html')

@transaction.atomic
def registro(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        Datos_form = Datos(request.POST,request.FILES or None)

        if form.is_valid() and Datos_form.is_valid():
            user=form.save()
            username = request.POST['username']
            password = request.POST['password1']

            user.refresh_from_db()
            Datos_form = Datos(request.POST,request.FILES or None,instance=user.usuarios)
            Datos_form.full_clean()
            Datos_form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return render(request, 'cuentas/index.html')
            return redirect(reverse('cuentas:index'))
    else:
        form = UserForm()
        Datos_form = Datos()
        args = {'UserForm_form': form,'Datos_form': Datos_form}
        return render(request, 'cuentas/reg_form.html', args)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'cuentas/index.html')
            else:
                return render(request, 'cuentas/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'cuentas/login.html', {'error_message': 'Invalid login'})
    return render(request, 'cuentas/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'cuentas/login.html')
