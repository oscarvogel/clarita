from django.conf.urls import url

from apps.ecommerce.views import lista_productos, detalle_producto

app_name = 'shop'

urlpatterns = [
    url(r'^$', lista_productos, name='lista_productos'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',detalle_producto,name='detalle_producto'),
    url(r'^(?P<slug_categoria>[-\w]+)/$',lista_productos,name='producto_lista_x_categoria'),
]
