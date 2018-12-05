from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile para el usuario {}'.format(self.usuario.username)