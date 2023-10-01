from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic.list import ListView  # Lista los registros que obtiene
from django.views.generic.detail import DetailView  # Detalle de los registros
from django.views.generic.edit import DeleteView, UpdateView, CreateView  # Borra, Actualiza y Crea registros
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm # Importamos formularios de autenticacion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Cliente, Productos, Proveedores
from .forms import ClienteFormulario, UserEditForm

# Create your views here.
def cliente(req, apellido, nombre, telefono):
    cliente=Cliente(apellido=apellido, nombre=nombre, telefono=telefono)
    cliente.save()    
    return HttpResponse(f"""
    <p>Cliente: {cliente.apellido} {cliente.nombre} {cliente.telefono} Agregado!!</p>
    """)

def producto(req, codigo, descripcion, precio):
    producto=Productos(codigo=codigo, descripcion=descripcion, precio=precio)
    producto.save()
    return HttpResponse(f"""
    <p>Producto: {productos.codigo} {productos.descripcion} {productos.precio} Agregado!!</p>
    """)

def proveedores(req, apellido, nombre, telefono):
    proveedores=Proveedores(apellido=apellido, nombre=nombre, telefono=telefono)
    proveedores.save()    
    return HttpResponse(f"""
    <p>Proveedor: {proveedores.apellido} {proveedores.nombre} {proveedores.telefono} Agregado!!</p>
    """)
@login_required
def lista_clientes(req):
    lista=Cliente.objects.all()
    return render(req, 'lista_clientes.html', {'lista_clientes': lista})

def inicio(req):
    return render(req, 'inicio.html')

def clientes(req):
    lista=Cliente.objects.all()
    return render(req, 'lista_clientes.html', {'lista_clientes': lista})

def productos(req):
    lista=Productos.objectsall()
    return render(req, 'productos.html', {'productos': lista})


def proveedores(req):
    return render(req, 'proveedores.html')

def aboutme(req):
    return render(req, 'aboutme.html')

def cliente_form(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
      
        miFormulario=ClienteFormulario(req.POST)
      
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data=miFormulario.cleaned_data
            cliente=Cliente(apellido=data['apellido'], nombre=data['nombre'], telefono=data['telefono'])
            cliente.save()
            return render(req, 'inicio.html', {'mensaje': 'Cliente agregado con exito.'})
        else:
          return render(req, 'inicio.html', {'mensaje': 'formulario invalido'})
    else:
        miFormulario=ClienteFormulario()

        return render(req, 'cliente_form.html', {'miFormulario': miFormulario})



def buscar_cliente(req):
    return render(req, 'buscar_cliente.html')

def buscar(req):
    if req.GET["apellido"]:
        apellido=req.GET["apellido"]
        clies=Cliente.objects.filter(apellido__icontains=apellido)
        if clies:

            return render(req, 'resultdoBusqueda.html', {'clies': clies})
    else:
        return HttpResponse('No se encontro nada')
    
def eliminaCliente(req, id):
    if req.method == 'POST':
        cliente = Cliente.objects.get(id=id)
        cliente.delete()

        lista=Cliente.objects.all()
        return render(req, 'lista_clientes.html', {'lista_clientes': lista})
    
def editarCliente(req, id):
    
    cliente = Cliente.objects.get(id=id)
    
    if req.method == 'POST':
      
        miFormulario=ClienteFormulario(req.POST)
      
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data=miFormulario.cleaned_data
            cliente.nombre=data['nombre']
            cliente.apellido=data['apellido']
            cliente.telefono=data['telefono']
            cliente.save()
            return render(req, 'inicio.html', {'mensaje': 'Cliente actualizado con exito.'})
        else:
          return render(req, 'inicio.html', {'mensaje': 'formulario invalido'})
    else:
        miFormulario=ClienteFormulario(initial={
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'telefono': cliente.telefono,
        })

        return render(req, 'editarCliente.html', {'miFormulario': miFormulario, 'id': cliente.id})

class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "cliente_detail.html"
    context_object_name = 'cliente'

class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'cliente_create.html'
    fields = ['nombre', 'apellido', 'telefono']  # campos a completar en el formulario cuando renderiza cliente_create.html
    success_url = '/app-tercera/'

class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'cliente_update.html'
    fields = ('__all__')
    success_url = '/app-tercera/'

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    success_url = '/app-tercera/'

def loginView(req):
    if req.method=='POST':
        miFormulario=AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            
            data=miFormulario.cleaned_data
            usuario = data['username']
            psw = data['password']
            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, 'inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(req, 'inicio.html', {'mensaje': 'Datos incorrectos'})
        else:
          return render(req, 'inicio.html', {'mensaje': 'formulario invalido'})

    else:
        miFormulario=AuthenticationForm()
        return render(req, 'login.html', {'miFormulario': miFormulario})
    
def register(req):
    if req.method=='POST':
        miFormulario=UserCreationForm(req.POST)

        if miFormulario.is_valid():
            
            data=miFormulario.cleaned_data
            usuario = data['username']
            miFormulario.save()
                
            return render(req, 'inicio.html', {'mensaje': f'Usuario: {usuario} creado con exito!'})
        else:
            return render(req, 'inicio.html', {'mensaje': 'Formulario invalido'})

    else:
        miFormulario=UserCreationForm()
        return render(req, 'registro.html', {'miFormulario': miFormulario})
    
def editar_perfil(req):

    usuario = req.user
    
    if req.method == 'POST':
      
        miFormulario=UserEditForm(req.POST, instance=req.user)
      
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.email=data['email']
            usuario.set_password(data['password1'])
            usuario.save()
            return render(req, 'inicio.html', {'mensaje': 'Perfil actualizado con exito.'})
        else:
          return render(req, 'editarPerfil.html', {'miFormulario': miFormulario})
    else:
        miFormulario=UserEditForm(instance=req.user)

        return render(req, 'editarPerfil.html', {'miFormulario': miFormulario})