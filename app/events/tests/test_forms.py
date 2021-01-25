import pytest

from app.events.forms import EventForm
from app.users.tests.factories import UserFactory
from app.events.tests.factories import EventFactory


@pytest.mark.django_db
class TestEventCreationForm:
    def test_create_event(self):
        """[summary]
        Test event create form
        """

        event = EventFactory.build()
        user = UserFactory.build()

        form = EventForm(
            {
                "owner": user,
                "title": event.title,
                "description": event.description,
                "date": event.date,
            }
        )

        assert form.is_valid()
