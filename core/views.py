from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import LugarPatrimonial, Categoria
from django.core.exceptions import PermissionDenied
from django.db.models import Q


# Create your views here.
def principal(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/principal.html', {'categorias': categorias})

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


def patrimonio(request, pk):
    pass


def gestion(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    return render(request, 'core/gestion.html')


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