from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from FindBikeFriends_advertisement.views import IndexView,LogoutView,CreateAdvertisementView,AdvertisementListView,AdvertisementDetailView,SettingsCompanyView

app_name = 'FindBikeFriends_advertisement'

urlpatterns = [
    url(r'^$', IndexView, name='dashboard'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^yeni-reklam/$', CreateAdvertisementView, name='new_advertisement'),
    url(r'^reklamlar/$', AdvertisementListView, name='advertisement_list'),
    url(r'^reklamlar/(?P<pk>\d+)/$', AdvertisementDetailView, name='advertisement_detail'),
    url(r'^ayarlar/$', SettingsCompanyView, name='settings_company'),
]
