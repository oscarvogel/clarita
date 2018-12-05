from django.shortcuts import render

# Create your views here.
from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(orden=order,producto=item['product'],precio=item['price'],
                    cantidad=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,'orders/order/creado.html',{'order': order})
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/crear.html',{'cart': cart, 'form': form})