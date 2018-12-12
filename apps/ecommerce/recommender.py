
import redis

from shop import settings
from .models import Producto

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                        port=settings.REDIS_PORT,
                        db=settings.REDIS_DB)

class Recommender(object):

    def get_product_key(self, id):
        return 'producto:{}:pagado_con'.format(id)

    def producto_comprados(self, productos):
        producto_ids = [p.id for p in productos]

        for producto_id in producto_ids:
            for with_id in producto_ids:
                # Consigue los otros productos comprados con cada producto.
                if producto_id != with_id:
                    # puntuación de incremento para el producto comprado juntos
                    r.zincrby(self.get_product_key(producto_id),
                              with_id,
                              amount=1)

    def productos_sugeridos_para(self, productos, max_results=6):
        producto_ids = [p.id for p in productos]
        if len(productos) == 1:
            # solo 1 producto
            sugerencias = r.zrange(
                self.get_product_key(producto_ids[0]),0, -1, desc=True)[:max_results]
        else:
            # generar una clave temporal
            flat_ids = ''.join([str(id) for id in producto_ids])
            tmp_key = 'tmp_{}'.format(flat_ids)
            # productos múltiples, combinar puntajes de todos los productos
            # almacenar el conjunto surtido resultante en una clave temporal
            keys = [self.get_product_key(id) for id in producto_ids]
            r.zunionstore(tmp_key, keys)
            # eliminar IDS para los productos
            r.zrem(tmp_key, *producto_ids)
            # obtener los identificadores de producto por su puntuación, orden descendiente
            sugerencias = r.zrange(tmp_key, 0, -1,desc=True)[:max_results]
            # quitar la clave temporal
            r.delete(tmp_key)
        ids_productos_sugeridos = [int(id) for id in sugerencias]
        # Obtener productos y ordenar por orden de aparición.
        productos_sugeridos = list(Producto.objects.filter(id__in=ids_productos_sugeridos))
        productos_sugeridos.sort(key=lambda x:
        ids_productos_sugeridos.index(x.id))
        return productos_sugeridos

    def clear_purchases(self):
        for id in Producto.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))