from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from apps.cart.forms import CartAddProductForm
from apps.ecommerce.models import Categoria, Producto, Historial
from apps.ecommerce.recommender import Recommender


def lista_productos(request, slug_categoria=None):
    categoria = None
    busqueda = False
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    destacados = Producto.objects.filter(destacado=True)[:10]
    try:
        historial = Historial.objects.filter(usuario=request.user)[:6]
    except:
        historial = None
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        productos = productos.filter(categoria=categoria)

    if request.method == 'POST':
        busqueda = True
        productos = Producto.objects.filter(nombre__icontains=request.POST['busqueda'])
        if request.POST['categoria'] != '0':
            productos = productos.filter(categoria=request.POST['categoria'])
    else:
        if categoria:
            productos = Producto.objects.filter(categoria=categoria)
        else:
            productos = Producto.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(productos, 8)
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    if busqueda:
        return render(request, 'ecommerce/producto/busqueda.html', {
            'categoria': categoria,
            'categorias': categorias,
            'productos': productos,
        })
    else:
        return render(request,'ecommerce/producto/lista.html',{
            'categoria':categoria,
            'categorias':categorias,
            'productos':productos,
            'destacados':destacados,
            'historial':historial
        })

def detalle_producto(request, id, slug):
    producto = get_object_or_404(Producto,
                                id=id,
                                slug=slug,
                                disponible=True)
    cart_product_form = CartAddProductForm()
    if producto:
        try:
            histdia = Historial.objects.filter(producto=producto, usuario=request.user)
            if not histdia:
                guardahist = Historial()
                guardahist.producto = producto
                guardahist.usuario = request.user
                guardahist.save()
        except Exception:
            pass

    r = Recommender()
    productos_recomendados = r.productos_sugeridos_para([producto], 4)
    return render(request,'ecommerce/producto/detalle.html',{
        'producto': producto,
        'cart_product_form': cart_product_form,
        'productos_recomendados': productos_recomendados
    })