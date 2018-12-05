from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from apps.ecommerce.models import Categoria, Producto, Favoritos
from apps.ecommerce.resources import ProductoResource


class CategoriaAdmin(ImportExportModelAdmin):

    search_fields = ['nombre', 'slug']
    list_display = ['nombre','slug', 'principal']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['principal',]

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(ImportExportModelAdmin):
    search_fields = ['nombre','categoria__nombre']
    resource_class = ProductoResource
    list_display = ['nombre', 'slug', 'preciopub', 'stock','disponible', 'destacado']
    list_filter = ['disponible', 'creado', 'modificado']
    list_editable = ['preciopub', 'stock', 'disponible','destacado']
    prepopulated_fields = {'slug': ('nombre',)}
admin.site.register(Producto, ProductoAdmin)

class FavoritosAdmin(admin.ModelAdmin):
    list_display = ['usuario','producto','activo']
    list_filter = ['activo',]
    raw_id_fields = ['producto', 'usuario']
    list_editable = ['activo','producto']
    search_fields = ['producto__nombre']
admin.site.register(Favoritos, FavoritosAdmin)