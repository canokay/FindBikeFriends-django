from django.conf.urls import url

from FindBikeFriends_rider.views import LoginView, LogoutView, IndexView

app_name = 'FindBikeFriends_rider'

urlpatterns = [
    url(r'^$', IndexView, name='dashboard'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
]
