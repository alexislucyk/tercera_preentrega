from django.contrib import admin
from .models import Cliente, Productos, Proveedores
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Proveedores)