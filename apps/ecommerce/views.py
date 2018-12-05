from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from apps.cart.forms import CartAddProductForm
from apps.ecommerce.models import Categoria, Producto

def lista_productos(request, slug_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    destacados = Producto.objects.filter(destacado=True)[:10]
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        productos = productos.filter(categoria=categoria)

    if request.method == 'POST':
        productos = Producto.objects.filter(nombre__icontains=request.POST['busqueda'])
        if request.POST['categoria'] != '0':
            productos = productos.filter(categoria=request.POST['categoria'])
    else:
        if categoria:
            productos = Producto.objects.filter(categoria=categoria)
        else:
            productos = Producto.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(productos, 9)
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    return render(request,'ecommerce/producto/lista.html',{
        'categoria':categoria,
        'categorias':categorias,
        'productos':productos,
        'destacados':destacados
    })

def detalle_producto(request, id, slug):
    producto = get_object_or_404(Producto,
                                id=id,
                                slug=slug,
                                disponible=True)
    cart_product_form = CartAddProductForm()
    return render(request,'ecommerce/producto/detalle.html',{
        'producto': producto,
        'cart_product_form': cart_product_form
    })