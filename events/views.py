# Views.py is used for handling the logic of the application. It contains functions that process requests and return responses. In this case, it is used to handle the registration of events.

from rest_framework import generics
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, RegistrationDetailSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationDetailSerializer
