from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from FindBikeFriends_web.views import IndexView

app_name = 'FindBikeFriends_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage')
]
