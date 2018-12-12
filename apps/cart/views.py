from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.ecommerce.models import Producto
from apps.ecommerce.recommender import Recommender


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
    cart.add(product=producto,
             quantity=cd['quantity'],
             update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    productos_recomendados = r.productos_sugeridos_para(cart_products,
                                                  max_results=4)
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'productos_recomendados': productos_recomendados
    })