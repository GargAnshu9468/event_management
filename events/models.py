from django.utils import timezone
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    registered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('event', 'email')

    def __str__(self):
        return f"{self.name} - {self.event.name}"
