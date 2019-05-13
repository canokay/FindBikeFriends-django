from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from FindBikeFriends_web.forms import LoginForm, ContactForm
from FindBikeFriends_app.models import Event

def IndexView(request):
    context = {
        "event": Event.objects.all()
    }
    return render(request, 'web/index.html',context)


def AboutView(request):
    return render(request, 'web/about.html')


def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return redirect('FindBikeFriends_web:contact')
    context = {
        "form": form
    }
    return render(request, 'web/contact.html',context)


def LoginView(request):
    return render(request, 'web/login.html')


def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Kullanıcı Adı veya Şifre Hatalı.')
            return render(request, 'web/login.html', context)
        login(request, user)
        return redirect('FindBikeFriends_web:homepage')
    return render(request, 'web/login.html', context)





def RegisterView(request):
    return render(request, 'web/register.html')
