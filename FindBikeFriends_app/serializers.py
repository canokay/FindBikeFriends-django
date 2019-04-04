from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, IntegerField, CharField, EmailField, DateField, ImageField
from rest_framework.serializers import ModelSerializer, Serializer

from FindBikeFriends_core.models import User, Followers, EventTag, Event, City, CompanyAddress, CompanyFeature, Company, Advertisement, AdvertisementImage

class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
