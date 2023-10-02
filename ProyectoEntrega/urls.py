
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from AppTercera.views import cliente, productos, proveedores, lista_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-tercera/', include('AppTercera.urls')),
]

urlpatterns+= static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
