from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Cliente, Productos, Proveedores
from .forms import ClienteFormulario
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
