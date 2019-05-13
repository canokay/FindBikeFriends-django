from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from FindBikeFriends_web.views import IndexView, LoginView, RegisterView, AboutView, ContactView

app_name = 'FindBikeFriends_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^hakkinda/$', AboutView, name='about'),
    url(r'^iletisim/$', ContactView, name='contact'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^register/$', RegisterView, name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)