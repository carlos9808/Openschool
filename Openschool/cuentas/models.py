from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    edad = models.IntegerField(null=True)
    perfil= models.ImageField()



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Usuarios.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
