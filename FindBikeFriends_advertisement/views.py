from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum

from FindBikeFriends_app.models import Company, Advertisement
from FindBikeFriends_advertisement.forms import CompanyForm, AdvertisementForm, AdvertisementImageForm, LoginForm


def LoginView(request):
    form = LoginForm()
    error_messages = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_user = authenticate(request, username=username, password=password)
            if login_user is not None and Advertisement.objects.filter(username=login_user.username).first():
                login(request, login_user)
            else:
                error_messages = "Kullanıcı adı ve Şifre Yanlış"
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'advertisement/login.html', {'form': form, 'error_messages': error_messages})



def LogoutView(request):
    logout(request)
    return redirect('FindBikeFriends_advertisement:login')


@login_required
def IndexView(request):
    context = {
        "advertisement_count": Advertisement.objects.filter(owner=request.user).count()
    }
    return render(request, 'advertisement/index.html',context)


@login_required
def CreateAdvertisementView(request):
    form = AdvertisementForm(request.POST or None, request.FILES)
    if form.is_valid():
        candidate_advertisement = form.save(commit=False)
        candidate_advertisement.owner = request.user
        candidate_advertisement.save()
        return redirect("FindBikeFriends_advertisement:advertisement_list")
    context = {
        "form": form
    }
    return render(request, 'advertisement/advertisement/new_advertisement.html',context)


@login_required
def AdvertisementListView(request):
    context = {
        "advertisement": Advertisement.objects.filter(owner=request.user)
    }
    return render(request, 'advertisement/advertisement/advertisement_list.html',context)





@login_required
def AdvertisementDetailView(request, pk):
    try:
        advertisement = Advertisement.objects.get(pk=pk)
    except Advertisement.DoesNotExist:
        return redirect('FindBikeFriends_advertisement:dashboard')
    if advertisement.owner.pk != request.user.pk:
        return redirect('FindBikeFriends_advertisement:dashboard')
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        "advertisement": Advertisement.objects.get(pk=pk)
    }
    return render(request, 'restaurant/advertisement/advertisement_detail.html', context)





@login_required
def SettingsCompanyView(request):
    return render(request, 'advertisement/settings/settings_account.html')
