from django.urls import path
from . import views

app_name = 'cuentas'


urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

    ]
