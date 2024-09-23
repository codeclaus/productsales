from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuarioForm
# Create your views here.
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from shoppcar.car import ShoppCar


def home(request):
    car = ShoppCar(request)
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # Redirige a la página principal después del registro
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})


def logear(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                # Redirige a la página principal después del inicio de sesión
                return redirect('home')
            else:
                messages.error(request, "ingresa algo valido")
                # Redirige a la página principal después del inicio de sesión
        else:
            messages.error(request, "eso no es valido")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def close_sesion(request):
    logout(request)
    return redirect("home")


# def enviar_correo(request):
#     subject = 'Asunto del correo'
#     message = 'UNA ORDEN DE CHULETA PARA LA CALLA 32'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['jhonbttm1998@gmail.com',]

#     send_mail(subject, message, email_from, recipient_list)

#     return HttpResponse('Correo enviado!')
