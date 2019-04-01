from django.contrib import admin
from django.contrib.auth.models import User, Group

from FindBikeFriends_core.models import User, Followers, EventTag, Event, City, CompanyAddress, CompanyFeature, Company, Advertisement, AdvertisementImage


admin.site.register(User)
admin.site.register(Followers)
admin.site.register(EventTag)
admin.site.register(Event)
admin.site.register(City)
admin.site.register(CompanyAddress)
admin.site.register(CompanyFeature)
admin.site.register(Company)
admin.site.register(Advertisement)
admin.site.register(AdvertisementImage)


admin.site.unregister(Group)
