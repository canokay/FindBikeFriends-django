from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from FindBikeFriends_core.models import Company, Advertisement
from FindBikeFriends_advertisement.forms import CompanyForm, AdvertisementForm, AdvertisementImageForm

@login_required
def IndexView(request):
    return render(request, 'advertisement/index.html')


@login_required
def LogoutView(request):
    logout(request)
    return redirect('FindBikeFriends_web:homepage')



@login_required
def CreateAdvertisementView(request):
    form = AdvertisementForm(request.POST or None, request.FILES)
    if form.is_valid():
        candidate_advertisement = form.save(commit=False)
        candidate_advertisement.owner = request.user
        candidate_advertisement.save()
        return redirect("new_advertisement")
    context = {
        "form": form
    }
    return render(request, 'advertisement/advertisement/new_advertisement.html',context)


@login_required
def AdvertisementListView(request):
    return render(request, 'advertisement/advertisement/advertisement_list.html')





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
    company = Company.objects.get(id=request.user.id)
    form = CompanyForm(request.POST or None,request.FILES or None,instance=company)
    if form.is_valid():
        form = form.save()
        return redirect("settings_account")
    context = {
        "form": form,
        "company": company
    }
    return render(request, 'advertisement/settings/settings_account.html', context)
