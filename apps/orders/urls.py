from django.urls import path

from apps.orders import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf, name='admin_order_pdf'),
    path('pedidos_cliente/', views.verpedidoscliente, name='pedidoscliente')
]