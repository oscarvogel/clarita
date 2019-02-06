from django.conf import settings
from django.db import models

# Create your models here.
from apps.ecommerce.models import Producto

LOCALIDADES_REPARTO = (
    ('Puerto Rico','Puerto Rico'),
)

LUGAR_ENTREGA = (
    ('A', 'Retira en el supermercado'),
    ('O', 'Reparto hasta mi casa'),
)
class Order(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250, default='')
    codigopostal = models.CharField(max_length=20, default='')
    ciudad = models.CharField(max_length=100, default='', choices=LOCALIDADES_REPARTO)
    creado = models.DateTimeField(auto_now_add=True)
    telefono = models.CharField(max_length=100, default='')
    nota = models.TextField(default='', blank=True)
    actualizado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)
    lugarentrega = models.CharField(max_length=1, choices=LUGAR_ENTREGA, default='O')

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return 'Orden {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    orden = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='order_items',on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.precio * self.cantidad