from django import forms
from .models import Event


class DateInput(forms.DateInput):
    """[summary]
    Add usable date field to the form
    """

    input_type = "date"


class EventForm(forms.ModelForm):
    """[summary]
    Event Add / update form
    """

    class Meta:
        model = Event
        fields = ["title", "description", "date"]
        widgets = {"date": DateInput()}
