from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from FindBikeFriends_advertisement.views import IndexView

app_name = 'FindBikeFriends_advertisement'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
]
