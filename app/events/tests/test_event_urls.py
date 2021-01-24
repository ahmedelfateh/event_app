import pytest
from django.urls import resolve, reverse

from app.events.models import Event

pytestmark = pytest.mark.django_db


def test_detail(event: Event):
    assert reverse("events:event", kwargs={"pk": event.id}) == f"/event/{event.id}"
    assert resolve(f"/event/{event.id}").view_name == "events:event"


def test_update(event: Event):
    assert (
        reverse("events:update", kwargs={"pk": event.id})
        == f"/event/update/{event.id}/"
    )
    assert resolve(f"/event/update/{event.id}/").view_name == "events:update"


def test_delete(event: Event):
    assert (
        reverse("events:delete", kwargs={"pk": event.id})
        == f"/event/delete/{event.id}/"
    )
    assert resolve(f"/event/delete/{event.id}/").view_name == "events:delete"


def test_add():
    assert reverse("events:add") == "/event/add/"
    # assert resolve("/events/add/").view_name == "events:add"