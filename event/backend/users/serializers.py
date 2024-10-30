from rest_framework import serializers

from events.models import Event
from users.models import TGUser



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)
    class Meta:
        model = TGUser
        fields = ['id', 'role', 'events']
