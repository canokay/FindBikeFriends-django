from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from FindBikeFriends_core.models import Event

class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
