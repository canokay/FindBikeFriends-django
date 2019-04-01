from django.shortcuts import render

def IndexView(request):
    return render(request, 'web/index.html')
