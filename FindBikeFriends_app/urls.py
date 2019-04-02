from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from rest_framework import routers

from FindBikeFriends import settings

app_name = 'FindBikeFriends_app'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^api/v1/', include('FindBikeFriends_app.v1.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
