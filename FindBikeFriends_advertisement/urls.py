from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from FindBikeFriends_advertisement.views import IndexView,LogoutView

app_name = 'FindBikeFriends_advertisement'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^logout/$', LogoutView, name='logout'),
]
