from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include("FindBikeFriends_web.urls")),
    url(r'^bisikletli/', include("FindBikeFriends_rider.urls")),
    url(r'^reklamveren/', include("FindBikeFriends_advertisement.urls")),
    url(r'^api/', include("FindBikeFriends_app.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
