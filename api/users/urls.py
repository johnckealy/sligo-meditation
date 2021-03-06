from django.urls import path
from .views import EventView, ContactForm



urlpatterns = [
    path('events/', EventView.as_view(), name='events'),
    path('contact_form_details/', ContactForm.as_view(), name='contact_form_detail'),
]
