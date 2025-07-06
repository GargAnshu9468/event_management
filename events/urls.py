from .views import EventListCreateView, RegisterAttendeeView, EventAttendeesView
from django.urls import path


urlpatterns = [
    path('events/', EventListCreateView.as_view()),
    path('events/<int:event_id>/register/', RegisterAttendeeView.as_view()),
    path('events/<int:event_id>/attendees/', EventAttendeesView.as_view()),
]
