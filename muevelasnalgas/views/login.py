from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def mainView(request):
    if request.user.is_authenticated:
        return redirect('/comunidades/')
    return redirect('/cuenta/login')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('../../')