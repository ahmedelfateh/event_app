from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Event(models.Model):

    owner = models.ForeignKey(
        "users.User", related_name="owner", on_delete=models.PROTECT
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField()
    participants = models.ManyToManyField("users.User", "participants", blank=True)

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
        return self.owner.email.split("@")[0]

    @property
    def participants_users(self):
        return self.participants.all()
