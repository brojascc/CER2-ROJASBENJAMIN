from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def principal(request):
    return render(request, 'core/principal.html')

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
            return render(request, 'core/principal.html')

    return render(request, 'core/registrar.html')



def iniciarSesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        usuario = authenticate(request, username=nombre, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return render(request, 'core/principal.html')
        else:
            return render(request, 'core/login.html', {'error': 'Credenciales invalidas'})

    return render(request, 'core/login.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def gestion(request):
    return render(request, 'core/gestion.html')