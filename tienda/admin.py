from django.contrib import admin
from tienda.models import Categoria, Producto, Cliente, Venta



admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)

# Register your models here.
