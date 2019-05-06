from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from FindBikeFriends_app.models import Event,EventType

class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'start_date',
            'type',
            'guests'
        ]
