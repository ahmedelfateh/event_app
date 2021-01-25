from app.events.models import Event
import pytest

from .factories import EventFactory
from app.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_event_creation():
    """[summary]
    Test event model, object create
    """

    owner = UserFactory(email="elfateh@gmail.com")
    event = EventFactory(owner=owner)

    assert event.owner == owner
    assert event.owner.email == "elfateh@gmail.com"


@pytest.mark.django_db
def test_user_get_absolute_url(event: Event):
    """[summary]
    test event models return correct get_absolute_url()
    """

    assert event.get_absolute_url() == f"/event/{event.id}"
