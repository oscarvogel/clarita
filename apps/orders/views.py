import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from apps.cart.cart import Cart
from apps.ecommerce.recommender import Recommender
from apps.ecommerce.render import Render
from apps.orders.forms import OrderCreateForm
from apps.orders.models import OrderItem, Order
from shop import settings


def order_create(request):
    cart = Cart(request)
    if not request.user.is_authenticated:
        return redirect('cuenta:dashboard')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.usuario = request.user
            order.pagado = False
            order.creado = datetime.datetime.now()
            order.actualizado = datetime.datetime.now()
            order.save()
            productos_comp = []
            for item in cart:
                OrderItem.objects.create(orden=order,producto=item['product'],precio=item['price'],
                    cantidad=item['quantity'])
                productos_comp.append(item['product'])
            if settings.USE_REDIS:
                r = Recommender()
                r.producto_comprados(productos_comp)

            # clear the cart
            send_mail(
                'Se ha producido una venta',
                'Un cliente ha comprado algo en la web podes modificarla aca {0}admin/orders/order/{1}/pdf/'.format(
                    settings.BASE_URL, order.id
                ),
                'info@ferreteriaavenida.com.ar',
                settings.ADMINS,
                fail_silently=False,
            )
            cart.clear()
            return render(request,'orders/order/creado.html',{'order': order})
        else:
            messages.warning(request, 'Debe corregir los datos para poder finalizar la compra.')
    else:
        ultimacompra = None
        try:
            ultimacompra = Order.objects.filter(usuario=request.user).order_by('-creado')
        except:
            pass
        if ultimacompra:
            form = OrderCreateForm(initial={'nombre':ultimacompra[0].nombre,
                                            'apellido':ultimacompra[0].apellido,
                                            'email':ultimacompra[0].email,
                                            'direccion':ultimacompra[0].direccion,
                                            'telefono':ultimacompra[0].telefono,
                                            'codigopostal':ultimacompra[0].codigopostal,
                                            'ciudad':ultimacompra[0].ciudad})
        else:
            form = OrderCreateForm()
    return render(request,'orders/order/crear.html',{'cart': cart, 'form': form})

# @staff_member_required
# def admin_order_pdf(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     html = render_to_string('orders/order/pdf.html',{'order': order})
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename=\
#         "order_{}.pdf"'.format(order.id)
#     weasyprint.HTML(string=html).\
#         write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
#     return response

def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    params = {
        'order':order,
        'request':request
    }

    return Render.render('orders/order/pdf.html', params)