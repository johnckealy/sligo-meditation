from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Event


admin.site.site_header = "Sligo Meditation | Admin Panel"

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Event)