from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from FindBikeFriends_rider.views import IndexView

app_name = 'FindBikeFriends_rider'

urlpatterns = [
    url(r'^$', IndexView, name='homepage')
]
