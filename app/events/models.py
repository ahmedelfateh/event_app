import datetime
from django.db import models
from django.urls import reverse
from app.users.models import User


class Event(models.Model):
    """[summary]
    Event Model
    """

    owner = models.ForeignKey(
        User, related_name="owner", on_delete=models.PROTECT, blank=True, null=True
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField()
    participants = models.ManyToManyField(User, "participants", blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "events"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:event", kwargs={"pk": self.id})

    @property
    def count_participants(self):
        return self.participants.count()

    @property
    def screen_name(self):
        return self.owner.email.split("@")[0]  # type: ignore

    @property
    def participants_users(self):
        return self.participants.all()

    @property
    def done_event(self):
        return self.date < datetime.date.today()
