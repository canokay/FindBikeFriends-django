from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from FindBikeFriends_rider.forms import  LoginForm


def LoginView(request):
    form = LoginForm()
    error_messages = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_user = authenticate(request, username=username, password=password)
            if login_user is not None:
                login(request, login_user)
            else:
                error_messages = "Kullanıcı adı ve Şifre Yanlış"
    if request.user.is_authenticated:
        return redirect('FindBikeFriends_rider:dashboard')
    return render(request, 'rider/login.html', {'form': form, 'error_messages': error_messages})


def LogoutView(request):
    logout(request)
    messages.success(request, "You are logout.")
    return ("FindBikeFriends_rider:login")


@login_required
def IndexView(request):
    return render(request, 'rider/index.html')
