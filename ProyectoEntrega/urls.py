
from django.contrib import admin
from django.urls import path, include
from AppTercera.views import cliente, productos, proveedores, lista_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-tercera/', include('AppTercera.urls')),
    
]
