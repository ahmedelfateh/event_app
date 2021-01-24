import pytest
from django.test import RequestFactory

from app.users.models import User
from app.events.models import Event
from app.users.tests.factories import UserFactory
from app.events.tests.factories import EventFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def event() -> Event:
    return EventFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()