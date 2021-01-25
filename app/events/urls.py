from django.urls import path
from .views import (
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    AddParticipant,
)

app_name = "events"

urlpatterns = [
    path("<int:pk>", EventDetailView.as_view(), name="event"),
    path("update/<int:pk>/", EventUpdateView, name="update"),
    path("delete/<int:pk>/", EventDeleteView, name="delete"),
    path("addparticipant/<int:pk>/", AddParticipant, name="addparticipant"),
    path("add/", EventCreateView.as_view(), name="add"),
]
