from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import LugarPatrimonial, Categoria
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import admin

def principal(request):
    categorias = Categoria.objects.all()
    patrimonios = LugarPatrimonial.objects.all()
    patrimonio_aleatorio = LugarPatrimonial.objects.order_by('?').first()
    return render(request, 'core/principal.html', {'categorias': categorias, 'patrimonios':patrimonios, 'patrimonio_aleatorio': patrimonio_aleatorio})

def registrar(request):
    if request.method == 'POST':
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            contraseña = request.POST.get('contraseña')
            contraseña2 = request.POST.get('contraseña2')

            if contraseña != contraseña2:
                return render(request, 'core/registrar.html', {'error': 'Las contraseñas son diferentes'})

            if User.objects.filter(username=nombre).exists():
                return render(request, 'core/registrar.html', {'error': 'Nombre de usuario ya existe'})

            usuario = User.objects.create_user(username=nombre, email=correo, password=contraseña)

            login(request, usuario)  
            return redirect('principal')

    return render(request, 'core/registrar.html')



def iniciarSesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        usuario = authenticate(request, username=nombre, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return redirect('principal')
        else:
            return render(request, 'core/login.html', {'error': 'Credenciales invalidas'})

    return render(request, 'core/login.html')



def detalle_patrimonio(request, pk):
    patrimonio = get_object_or_404(LugarPatrimonial.objects.select_related('categoria'), pk=pk)
    return render(request, 'core/detalle_patrimonio.html', {'patrimonio': patrimonio})

def catalogo(request):
    q = request.GET.get('q', '').strip()
    categoria_id = request.GET.get('categoria', '')

    patrimonios = LugarPatrimonial.objects.select_related('categoria').order_by('nombre')

    if q:
        patrimonios = patrimonios.filter(Q(nombre__icontains=q) | Q(descripcion__icontains=q))
    if categoria_id.isdigit():
        patrimonios = patrimonios.filter(categoria_id=categoria_id)

    return render(request, 'core/catalogo.html', {
            'patrimonios': patrimonios,
            'categorias': Categoria.objects.all(),
            'q': q,
            'categoria_id': categoria_id,
        })