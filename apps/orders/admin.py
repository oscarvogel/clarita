from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from apps.orders.models import OrderItem, Order


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Ventas'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['producto']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'email', 'direccion', 'codigopostal', 'ciudad', 'pagado',
        'creado', 'actualizado',]
    list_filter = ['pagado', 'creado', 'actualizado']
    raw_id_fields = ['usuario']
    list_editable = ['pagado',]
    inlines = [OrderItemInline]