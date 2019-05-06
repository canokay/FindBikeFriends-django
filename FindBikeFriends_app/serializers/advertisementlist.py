from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from FindBikeFriends_app.models import Advertisement


class AdvertisementListSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
