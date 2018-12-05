from django.contrib import admin

# Register your models here.
from apps.orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['producto']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'email', 'direccion', 'codigopostal', 'ciudad', 'pagado',
        'creado', 'actualizado']
    list_filter = ['pagado', 'creado', 'actualizado']
    raw_id_fields = ['usuario']
    inlines = [OrderItemInline]