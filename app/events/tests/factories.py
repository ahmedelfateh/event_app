from factory import Sequence, SubFactory
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from factory.django import DjangoModelFactory
from app.events.models import Event
from app.users.tests.factories import UserFactory


class EventFactory(DjangoModelFactory):
    """[summary]
    Create fake event for test
    """

    owner = SubFactory(UserFactory)
    title = Sequence(lambda n: "event {0}".format(n))
    description = Sequence(lambda n: "event {0}".format(n))
    date = timezone.now() + relativedelta(months=6)
    # participants = SubFactory(UserFactory)

    class Meta:
        model = Event
