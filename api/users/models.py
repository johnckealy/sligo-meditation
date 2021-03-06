import re
from django.db import models
from datetime import datetime
from django.utils import timezone

ICON_CHOICES = (
    ("self_improvement", "self_improvement"),
    ("spa", "spa"),
    ("piano", "piano"),
    ("fireplace", "fireplace"),
    ("coffee", "coffee"),
    ("grass", "grass"),
    ("brightness_2", "brightness_2"),
    ("auto_awesome", "auto_awesome"),
    ("brightness_4", "brightness_4"),
    ("palette", "palette"),
)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    zoom_link = models.CharField(max_length=600, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    icon = models.CharField(max_length=60, choices=ICON_CHOICES, default='self_improvement')

    def __str__(self):
        return self.title if self.title else 'No title'

    @property
    def is_past(self):
        if self.end_time < timezone.now():
            return True
        else:
            return False