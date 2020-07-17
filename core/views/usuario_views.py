from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.


def login_usuario(request):
    if request.method == "POST":
        nomeusuario = request.POST["username"]
        senhausuario = request.POST["password"]
        usuario = authenticate(
            request, username=nomeusuario, password=senhausuario)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais incorretas, corrija !')
            return redirect('login_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


@login_required()
def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {
        "form_usuario": form_usuario})
