from django.contrib import admin
from .models import Cliente, Productos, Proveedores, Avatar
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Avatar)