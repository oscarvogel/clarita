from django import template

from apps.ecommerce.models import Categoria, Favoritos
from shop import settings

register = template.Library()

datos_empresa = {'titulo_principal': settings.TITULO_PRINCIPAL,
           'nombre_sitio': settings.NOMBRE_SITIO,
           'web_empresa': settings.WEB_EMPRESA,
           'telefono_empresa': settings.TELEFONO_EMPRESA,
           'email_empresa': settings.EMAIL_EMPRESA,
           'domicilio_empresa': settings.DOMICILIO_EMPRESA}


@register.simple_tag
def telefono_empresa():
    return datos_empresa['telefono_empresa']

@register.simple_tag
def titulo_principal():
    return datos_empresa['titulo_principal']

@register.simple_tag
def web_empresa():
    return datos_empresa['web_empresa']

@register.simple_tag
def email_empresa():
    return datos_empresa['email_empresa']

@register.simple_tag
def domicilio_empresa():
    return datos_empresa['domicilio_empresa']

@register.inclusion_tag('base/navegacion.html')
def categorias_principales():
    categorias = Categoria.objects.filter(principal = True)
    return {'principales_categorias':categorias}

@register.simple_tag(takes_context=True)
def total_favoritos(context):
    user = context['user']
    if user:
        fa = Favoritos.objects.filter(usuario=user).count()
    else:
        fa = 0
    return fa

@register.filter(name='descuento')
def descuento(monto, porcentaje):
    print(monto, porcentaje)
    return round(monto - monto * porcentaje / 100, 2)