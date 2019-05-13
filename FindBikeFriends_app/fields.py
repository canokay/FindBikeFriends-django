from rest_framework.fields import ImageField
from FindBikeFriends import settings


class LeximageField(ImageField):
    def to_representation(self, value):
        if not value:
            return None
        domain = 'bitabak.net'
        protocol = 'http' if settings.DEBUG else 'https'
        return '%s://%s%s' % (protocol, domain, value.url)