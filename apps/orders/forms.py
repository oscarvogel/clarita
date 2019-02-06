from django import forms
from django.forms import ChoiceField, Select

from apps.orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellido', 'email', 'direccion','lugarentrega','codigopostal', 'ciudad', 'telefono', 'nota']
        widgets ={
            'ciudad': Select(attrs={'class':'form-control'}),
            'lugarentrega': Select(attrs={'class':'form-control'})
        }