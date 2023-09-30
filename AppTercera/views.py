from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Cliente, Productos, Proveedores
from .forms import ClienteFormulario
from django.views.generic.list import ListView  # Lista los registros que obtiene
from django.views.generic.detail import DetailView  # Detalle de los registros
from django.views.generic.edit import DeleteView, UpdateView, CreateView  # Borra, Actualiza y Crea registros

# Create your views here.
def cliente(req, apellido, nombre, telefono):
    cliente=Cliente(apellido=apellido, nombre=nombre, telefono=telefono)
    cliente.save()    
    return HttpResponse(f"""
    <p>Cliente: {cliente.apellido} {cliente.nombre} {cliente.telefono} Agregado!!</p>
    """)

def productos(req, codigo, descripcion, precio):
    productos=Productos(codigo=codigo, descripcion=descripcion, precio=precio)
    productos.save()
    return HttpResponse(f"""
    <p>Producto: {productos.codigo} {productos.descripcion} {productos.precio} Agregado!!</p>
    """)

def proveedores(req, apellido, nombre, telefono):
    proveedores=Proveedores(apellido=apellido, nombre=nombre, telefono=telefono)
    proveedores.save()    
    return HttpResponse(f"""
    <p>Proveedor: {proveedores.apellido} {proveedores.nombre} {proveedores.telefono} Agregado!!</p>
    """)

def lista_clientes(req):
    lista=Cliente.objects.all()
    return render(req, 'lista_clientes.html', {'lista_clientes': lista})

def inicio(req):
    return render(req, 'inicio.html')

def clientes(req):
    lista=Cliente.objects.all()
    return render(req, 'lista_clientes.html', {'lista_clientes': lista})

def productos(req):
    return render(req, 'productos.html')

def proveedores(req):
    return render(req, 'proveedores.html')

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

class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"
    context_object_name = 'cliente'

class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'cliente_create.html'
    fields = ['nombre', 'apellido', 'telefono']  # campos a completar en el formulario cuando renderiza cliente_create.html
    success_url = '/AppTercera/'

class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'cliente_update.html'
    fields = ['__all__']
    success_url = '/AppTercera/'

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    success_url = '/AppTercera/'













