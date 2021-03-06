from rest_framework import generics
from rest_framework.response import Response
from .serializers import EventSerializer, ContactFormSerializer
from .models import Event
from django.core.mail import send_mail
from django.utils.html import escape


class EventView(generics.GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        events = self.queryset.all()
        resp = EventSerializer(events, many=True).data
        return Response(resp)


class ContactForm(generics.GenericAPIView):

    serializer_class = ContactFormSerializer

    def get(self, request):
        return Response(True)

    def post(self, request):
        email = request.data['email']
        message = escape(request.data['message'])
        body = f'\nFrom: {email} \n\n{message} \n [This email was generated automatically by the Sligo Meditation website.]'

        send_mail('Message from the Sligo Meditation Website', body, 'johnckealy.dev@gmail.com', ['johnckealy.dev@gmail.com'])
        return Response(True)