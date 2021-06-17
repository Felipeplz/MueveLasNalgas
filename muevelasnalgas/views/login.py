from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db import reset_queries
from django.shortcuts import redirect, render

def loginView(request):
    if not 'respuesta' in request.session:
        request.session['respuesta'] = ""
    return render(request, 'login.html', {'respuesta':request.session['respuesta']})

def login(request):
    user = request.POST['usuario']
    pwrd = request.POST['contraseña']
    usuario = authenticate(request, username=user, password=pwrd)
    if usuario is not None:
        auth_login(request, user)
        return redirect('/mapa/')
    else:
        request.session['respuesta'] = "La combinación de usuario y contraseña no es válida."
        return loginView(request)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')