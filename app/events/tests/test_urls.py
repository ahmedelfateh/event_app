import pytest
from django.urls import resolve, reverse

from app.events.models import Event

pytestmark = pytest.mark.django_db


def test_detail(event: Event):
    """[summary]
    Test /event/{event.id}/ return the correct view ("events:event")
    """

    assert reverse("events:event", kwargs={"pk": event.id}) == f"/event/{event.id}"
    assert resolve(f"/event/{event.id}").view_name == "events:event"


def test_update(event: Event):
    """[summary]
    Test /event/update/ return the correct view ("events:update")
    """

    assert (
        reverse("events:update", kwargs={"pk": event.id})
        == f"/event/update/{event.id}/"
    )
    assert resolve(f"/event/update/{event.id}/").view_name == "events:update"


def test_delete(event: Event):
    """[summary]
    Test /event/delete/ return the correct view ("events:delete")
    """

    assert (
        reverse("events:delete", kwargs={"pk": event.id})
        == f"/event/delete/{event.id}/"
    )
    assert resolve(f"/event/delete/{event.id}/").view_name == "events:delete"


def test_add():
    """[summary]
    Test /event/add/ return the correct view ("events:add")
    """
    assert reverse("events:add") == "/event/add/"