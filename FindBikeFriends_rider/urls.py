from django.conf.urls import url

from FindBikeFriends_rider.views import LoginView, LogoutView, IndexView, EventListView, EventDetailView

app_name = 'FindBikeFriends_rider'

urlpatterns = [
    url(r'^$', IndexView, name='dashboard'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^event/$', EventListView, name='event_list'),
    url(r'^event/(?P<id>\d+)/$', EventDetailView, name='event_detail'),
]
