from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def IndexView(request):
    return render(request, 'advertisement/index.html')

def LogoutView(request):
    logout(request)
    return redirect('FeedbackApp_web:homepage')
