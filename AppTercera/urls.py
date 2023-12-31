
from django.urls import path
from django.contrib.auth.views import LogoutView
from AppTercera.views import *

urlpatterns = [
    path('cliente/', clientes, name='Pag_Cliente'),
    path('producto/', productos, name='Pag_Productos'),
    path('proveedores/', proveedores, name='Pag_Proveedores'),
    path('lista-clientes/', lista_clientes, name='Lista_Clientes'),
    path('', inicio, name='Inicio'),
    path('cliente-form/', cliente_form, name='Pag_ClienteForm'),
    path('buscar-cliente/', buscar_cliente, name='Pag_BuscarCliente'),
    path('eliminar-cliente/<int:id>', eliminaCliente, name='Eliminar_Cliente'),
    path('editar-cliente/<int:id>', editarCliente, name='Editar_Cliente'),
    path('buscar/', buscar, name='Buscar'),
    path('lista-cliente/', ClienteList.as_view(), name='ListaCliente'), # Se invocan clases como funcion con el .as_view()
    path('detalle-cliente/<pk>', ClienteDetail.as_view(), name='DetalleCliente'),
    path('crea-cliente/', ClienteCreate.as_view(), name='CreaCliente'),
    path('actualiza-cliente/<pk>', ClienteUpdate.as_view(), name='ActualizaCliente'),
    path('elimina-cliente/<pk>', ClienteDelete.as_view(), name='EliminaCliente'),
    path('login/', loginView, name='Login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('registrar/', register, name='Registrar'),
    path('aboutme/', aboutme, name='AboutMe'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
]

