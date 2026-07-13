#this file is for serializers, i.e. converting complex data types like querysets and model instances into native Python datatypes that can then be easily rendered into JSON, XML or other content types. It also provides deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
from rest_framework import serializers
from .models import Event, Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class RegistrationDetailSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'event', 'user', 'seats_booked', 'status', 'timestamp', 'payment_status']

