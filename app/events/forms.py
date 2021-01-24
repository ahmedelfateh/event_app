from django import forms
from .models import Event


# creating a form
class EventForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Event
        fields = ["title", "description", "date"]
