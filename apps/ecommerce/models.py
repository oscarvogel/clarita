import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Categoria(models.Model):

    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    principal = models.BooleanField(default=False)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop:producto_lista_x_categoria',
                       args=[self.slug])

class Producto(models.Model):

    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    unidad = models.CharField(max_length=8, default='')
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    preciopub = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(blank=True, default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    destacado = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ('nombre',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop:detalle_producto',
                       args=[self.id, self.slug])

class Favoritos(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)

    class Meta:
        ordering = ('usuario',)

    def __str__(self):
        return self.producto.nombre

class Historial(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "Historial"
        ordering = ('-fecha',)

    def __str__(self):
        return '{}'.format(self.id)