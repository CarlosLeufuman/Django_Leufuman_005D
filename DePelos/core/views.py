from django.shortcuts import render , redirect
from django.views.decorators import csrf
from .models import Producto , Usuarios
from .forms import ProductoForm , UsuarioForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def somos(request):
    return render(request, 'somos.html')

def galeria(request):
    return render(request, 'galeria.html')

def registro(request):
    return render(request, 'registro.html')

def adminez(request):
    return render(request, 'adminez.html')

def mostrar_usuario(request):
    usuarios = Usuarios.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request, 'mostrar_usuario.html',datos)

def mostrar_producto(request):
    producto = Producto.objects.all()
    datos2 = {
        'producto': producto
    }
    return render(request, 'mostrar_producto.html',datos2)

def form_producto(request):                             
    if request.method== 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)

        if producto_form.is_valid():
            producto_form.save()
            return redirect ('mostrar_producto')

    else:
        producto_form = ProductoForm()
    return render(request, 'form_crear_productos.html' ,{'producto_form': producto_form })



def form_usuario(request):                             
    if request.method== 'POST':
        usuario_form = UsuarioForm(request.POST)

        if usuario_form.is_valid():
            usuario_form.save()
            return redirect ('mostrar_usuario')

    else:
        usuario_form = UsuarioForm()
    return render(request, 'form_crear_usuarios.html' ,{'usuario_form': usuario_form })

def form_del_usuario(request,id):
    usuarios = Usuarios.objects.get(email=id)
    usuarios.delete()
    return redirect('mostrar_usuario')

def form_del_producto(request,id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect('mostrar_producto')

def form_mod_usuario(request, id):
    usuarios = Usuarios.objects.get(email=id)
    datos = {
        'form': UsuarioForm(instance = usuarios)
    }
    if request.method=='POST':
        formulario = UsuarioForm(data=request.POST, instance = usuarios)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar_usuario')
        
    return render(request, 'form_mod_usuario.html', datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(id_producto=id)
    datos3 = {
        'form2': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar_producto')
        
    return render(request, 'form_mod_producto.html', datos3)