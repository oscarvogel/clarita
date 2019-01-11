from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

from apps.ecommerce.models import Categoria, Producto, Favoritos, Historial, Paramsist, LocalidadEntrega
from apps.ecommerce.resources import ProductoResource

def importa_imagen(obj):
    return mark_safe('<a href="{}">Importar</a>'.format(
        reverse('shop:admin_imagen_producto', args=[obj.id])))

class CategoriaAdmin(ImportExportModelAdmin):

    search_fields = ['nombre', 'slug']
    list_display = ['nombre','slug', 'principal']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['principal',]

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(ImportExportModelAdmin):
    search_fields = ['nombre','categoria__nombre']
    resource_class = ProductoResource
    list_display = ['nombre', 'slug', 'preciopub', 'stock','disponible', 'destacado', 'descuento']
    list_filter = ['disponible', 'creado', 'modificado', 'descuento']
    list_editable = ['preciopub', 'stock', 'disponible','destacado', 'descuento']
    prepopulated_fields = {'slug': ('nombre',)}
admin.site.register(Producto, ProductoAdmin)

class FavoritosAdmin(admin.ModelAdmin):
    list_display = ['usuario','producto','activo']
    list_filter = ['activo',]
    raw_id_fields = ['producto', 'usuario']
    list_editable = ['activo','producto']
    search_fields = ['producto__nombre']
admin.site.register(Favoritos, FavoritosAdmin)

class HistorialAdmin(admin.ModelAdmin):
    list_display = ['producto','usuario','fecha']
    search_fields = ['usuario',]
admin.site.register(Historial, HistorialAdmin)

class ParamsistAdmin(admin.ModelAdmin):
    list_display = ('clave', 'valor', 'detalle')
    search_fields = ('clave', 'valor')
    list_per_page = 20
admin.site.register(Paramsist, ParamsistAdmin)

class LocalidadEntregaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('nombre','montominimoflete')
    list_editable = ('montominimoflete',)
admin.site.register(LocalidadEntrega, LocalidadEntregaAdmin)

