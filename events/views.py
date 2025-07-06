from .serializers import EventSerializer, AttendeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Event, Attendee
from django.utils import timezone


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('start_time')
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')


class RegisterAttendeeView(generics.CreateAPIView):
    serializer_class = AttendeeSerializer

    def create(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']

        try:
            event = Event.objects.get(pk=event_id)

        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=404)

        if event.attendees.count() >= event.max_capacity:
            return Response({"error": "Event is full"}, status=400)

        if Attendee.objects.filter(event=event, email=request.data.get('email')).exists():
            return Response({"error": "This email is already registered for the event."}, status=400)

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(event=event)

        return Response(serializer.data, status=201)


class EventAttendeesView(generics.ListAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        return Attendee.objects.filter(event_id=self.kwargs['event_id']).order_by('-registered_at')
