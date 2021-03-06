from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Event



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    start_time = serializers.DateTimeField(format="%a %d %b at %I:%M%P")
    is_past = serializers.BooleanField(default=False)


class ContactFormSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'

    email = serializers.CharField()
    message = serializers.CharField()
