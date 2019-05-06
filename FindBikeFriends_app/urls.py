from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from FindBikeFriends import settings
from FindBikeFriends_app.api import EventListView,EventDetailView, AdvertisementListView, AdvertisementDetailView

app_name = 'FindBikeFriends_app'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^', include(router.urls)),
        url(r'^event/$', EventListView.as_view()),
        url(r'^event/(?P<id>\d+)/$', EventDetailView.as_view()),
        url(r'^reklam/$', AdvertisementListView.as_view()),
        url(r'^reklam/(?P<id>\d+)/$', AdvertisementDetailView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
