from django.conf.urls import url

from FindBikeFriends_web.views import IndexView, LoginView, RegisterView

app_name = 'FindBikeFriends_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^register/$', RegisterView, name='register'),
]
