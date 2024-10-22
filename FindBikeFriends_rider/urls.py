from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from FindBikeFriends_rider.views import LoginView, LogoutView, IndexView, EventListView, EventDetailView, EventCreateView

app_name = 'FindBikeFriends_rider'

urlpatterns = [
    url(r'^$', IndexView, name='dashboard'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^etkinlik/$', EventListView, name='event_list'),
    url(r'^etkinlik-ekle/$', EventCreateView, name='event_new'),
    url(r'^etkinlik/(?P<id>\d+)/$', EventDetailView, name='event_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)