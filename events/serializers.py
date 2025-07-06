from django.utils.timezone import localtime
from rest_framework import serializers
from .models import Event, Attendee


class EventSerializer(serializers.ModelSerializer):
    start_time_local = serializers.SerializerMethodField(read_only=True)
    end_time_local = serializers.SerializerMethodField(read_only=True)

    def get_start_time_local(self, obj):
        return localtime(obj.start_time).isoformat()

    def get_end_time_local(self, obj):
        return localtime(obj.end_time).isoformat()

    class Meta:
        model = Event
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    registered_at = serializers.SerializerMethodField()
    event = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_registered_at(self, obj):
        return localtime(obj.registered_at).isoformat()

    class Meta:
        model = Attendee
        fields = '__all__'
