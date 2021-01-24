from django.urls import path
from .views import (
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    AddParticipant,
)

app_name = "orders"

urlpatterns = [
    path("<pk>", EventDetailView.as_view(), name="event"),
    # path("<pk>", EventDetailView, name="event"),
    path("update/<pk>/", EventUpdateView, name="update"),
    # path("update/<int:pk>", EventUpdateView.as_view(), name="update"),
    path("delete/<pk>/", EventDeleteView, name="delete"),
    # path("delete/<pk>/", EventDeleteView.as_view(), name="delete"),
    path("addparticipant/<pk>/", AddParticipant, name="addparticipant"),
    path("add/", EventCreateView.as_view(), name="add"),
]
