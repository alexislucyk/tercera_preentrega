
from django.urls import path
from AppTercera.views import *

urlpatterns = [
    path('cliente/', clientes, name='Pag_Cliente'),
    path('producto/', productos, name='Pag_Productos'),
    path('proveedores/', proveedores, name='Pag_Proveedores'),
    path('lista-clientes/', lista_clientes, name='Lista_Clientes'),
    path('', inicio, name='Inicio'),
    path('cliente-form/', cliente_form, name='Pag_ClienteForm'),
    path('buscar-cliente/', buscar_cliente, name='Pag_BuscarCliente'),
    path('buscar/', buscar, name='Buscar'),
]
