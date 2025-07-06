from rest_framework.test import APIClient
from events.models import Event, Attendee
from django.utils import timezone
from datetime import timedelta
import pytest


@pytest.mark.django_db
class TestEventAPI:
    def setup_method(self):
        self.client = APIClient()

    def create_event(self, name="Test Event 1", location="Bangalore", max_capacity=5):
        return Event.objects.create(
            name=name,
            location=location,
            start_time=timezone.now() + timedelta(days=1),
            end_time=timezone.now() + timedelta(days=1, hours=2),
            max_capacity=max_capacity
        )

    def test_create_event(self):
        url = '/api/events/'

        data = {
            "name": "Test Event 2",
            "location": "Bangalore",
            "start_time": (timezone.now() + timedelta(days=1)).isoformat(),
            "end_time": (timezone.now() + timedelta(days=1, hours=2)).isoformat(),
            "max_capacity": 5
        }

        response = self.client.post(url, data, format='json')

        assert response.status_code == 201
        assert response.data['name'] == "Test Event 2"

    def test_list_events(self):
        self.create_event(name="Test Event 3")

        url = '/api/events/'
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data['results']) >= 1

    def test_register_attendee_successfully(self):
        event = self.create_event()
        url = f'/api/events/{event.id}/register/'

        data = {
            "name": "Anshu Garg",
            "email": "a.kgarg9050@gmail.com",
            "event": event.id
        }

        response = self.client.post(url, data, format='json')

        assert response.status_code == 201
        assert Attendee.objects.filter(email="a.kgarg9050@gmail.com").exists()

    def test_prevent_duplicate_registration(self):
        event = self.create_event()
        url = f'/api/events/{event.id}/register/'

        data = {
            "name": "Anshu Garg",
            "email": "a.kgarg9050@gmail.com",
            "event": event.id
        }

        self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')

        assert response.status_code == 400
        assert "already registered" in str(response.data).lower()

    def test_prevent_overbooking(self):
        event = self.create_event(max_capacity=1)
        url = f'/api/events/{event.id}/register/'

        data1 = {
            "name": "User 1",
            "email": "user1@gmail.com",
            "event": event.id
        }

        data2 = {
            "name": "User 2",
            "email": "user2@gmail.com",
            "event": event.id
        }

        self.client.post(url, data1, format='json')
        response = self.client.post(url, data2, format='json')

        assert response.status_code == 400
        assert "event is full" in str(response.data).lower()

    def test_list_event_attendees(self):
        event = self.create_event()

        Attendee.objects.create(name="Attendee 1", email="attendee1@gmail.com", event=event)
        Attendee.objects.create(name="Attendee 2", email="attendee2@gmail.com", event=event)

        url = f'/api/events/{event.id}/attendees/'
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data['results']) == 2
