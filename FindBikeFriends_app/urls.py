from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from FindBikeFriends import settings
from FindBikeFriends_app.views import EventListView

app_name = 'FindBikeFriends_app'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^', include(router.urls)),
        url(r'^events/$', EventListView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
