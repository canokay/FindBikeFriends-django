import datetime
import uuid
from urllib.parse import quote

from django.contrib.auth.models import update_last_login
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from FindBikeFriends import settings
from FindBikeFriends_app.models import User, Followers,  Event, City, CompanyAddress, CompanyFeature, Company, Advertisement, AdvertisementImage

from FindBikeFriends_app.serializers.eventlist import EventListSerializer
from FindBikeFriends_app.serializers.eventdetail import EventDetailSerializer
from FindBikeFriends_app.serializers.eventcreate import EventCreateSerializer
from FindBikeFriends_app.serializers.advertisementlist import AdvertisementListSerializer
from FindBikeFriends_app.serializers.advertisementdetail import AdvertisementDetailSerializer



class EventListView(ListAPIView):
    serializer_class = EventListSerializer

    def get_queryset(self):
        type = self.request.GET.get('type', None)
        return Event.objects.all()



class EventDetailView(ListAPIView):
    serializer_class = EventDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Event.objects.filter(id=id)




class AdvertisementListView(ListAPIView):
    serializer_class = AdvertisementListSerializer

    def get_queryset(self):
        type = self.request.GET.get('type', None)
        def convertFloat(val):
            try:
                return float(val)
            except:
                return None

        def parseDate(val):
            try:
                return parse_date(val)
            except:
                return None

        start_date = parseDate(self.request.GET.get('start_date', None))
        today = timezone.now()

        if not start_date:
            data = Advertisement.objects.filter(start_date__gte=today, is_active=True).order_by('start_date')
        elif not start_date:
            data = Advertisement.objects.filter(start_date__gte=today, is_active=True).order_by('start_date')
        else:
            data = Advertisement.objects.filter(start_date__day=start_date.day, start_date__month=start_date.month,
                                        start_date__year=start_date.year, is_active=True)

        return data


class AdvertisementDetailView(ListAPIView):
    serializer_class = AdvertisementDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Advertisement.objects.filter(id=id)



class EventCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EventCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
