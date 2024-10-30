from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from events.models import Event
from events.serializers import EventSerializer


# Create your views here.

class CreateEventApiView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListApiView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailApiView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UpdateEventApiView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DeleteEventApiView(DestroyAPIView):
    queryset = Event.objects.all()
