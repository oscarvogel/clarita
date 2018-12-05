from django import forms

from apps.orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellido', 'email', 'direccion','codigopostal', 'ciudad', 'telefono', 'nota']