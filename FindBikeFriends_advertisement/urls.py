from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from FindBikeFriends_advertisement.views import IndexView,LoginView,LogoutView,CreateAdvertisementView,AdvertisementListView,AdvertisementDetailView

app_name = 'FindBikeFriends_advertisement'

urlpatterns = [
    url(r'^$', IndexView, name='dashboard'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^yeni-reklam/$', CreateAdvertisementView, name='new_advertisement'),
    url(r'^reklamlar/$', AdvertisementListView, name='advertisement_list'),
    url(r'^reklamlar/(?P<id>\d+)/$', AdvertisementDetailView, name='advertisement_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)