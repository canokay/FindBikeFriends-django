from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from FindBikeFriends_app.models import Event,EventType


class EventTypeSerializer(ModelSerializer):
    class Meta:
        model = EventType
        fields = [
            'type',
        ]

class EventListSerializer(ModelSerializer):
    type=EventTypeSerializer()
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'description',
            'start_date',
            'type'
        ]
