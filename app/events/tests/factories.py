from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import Faker
from factory.django import DjangoModelFactory
from app.events.models import Event


class EventFactory(DjangoModelFactory):

    email = Faker("email")
    password = Faker(
        "password",
        length=42,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )

    class Meta:
        model = Event
