from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# * Importaciones del proyecto
from .forms import FormRegister

# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.warning(request, 'No te has identificado')

    return render(request, 'layouts/login.html')


def RegisterUser(request):
    register_form = FormRegister()

    if request.method == 'POST':
        register_form = FormRegister(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')

            return redirect('login')

    context = {
        "form_r": register_form
    }
    return render(request, 'layouts/register.html', context)


def Logout(request):
    logout(request)
    return redirect('login')
