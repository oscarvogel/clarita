from import_export import resources

from slugify import slugify

from apps.ecommerce.models import Producto, Categoria


class ProductoResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        row['slug'] = slugify(row['slug'])
        row['preciopub'] = round(row['preciopub'], 3)

    class Meta:
        model = Producto
        fields = ('id', 'categoria', 'nombre', 'slug', 'descripcion', 'stock', 'preciopub')

class CategoriaResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        row['slug'] = slugify(row['nombre'].lower())

    class Meta:
        model = Categoria