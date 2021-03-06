import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Event
from .forms import EventForm


class EventListView(ListView):
    """[summary]
    EventListView -> Event List

    List all events data
    Paginated 5

    url: /
    """

    model = Event
    paginate_by = 5
    ordering = ["-date"]
    template_name = "pages/home.html"


class EventDetailView(DetailView):
    """[summary]
    EventDetailView -> Event Detail

    Event detail

    url: /event/<int:pk>/
    pk = event.id
    """

    model = Event
    template_name = "pages/event.html"


class EventCreateView(LoginRequiredMixin, CreateView):
    """[summary]
    EventCreateView -> Event Create

    Create new Event

    url: /event/add/
    """

    model = Event
    template_name = "pages/add_event.html"
    form_class = EventForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        title = form.cleaned_data["title"]
        date = form.cleaned_data["date"]
        today = datetime.date.today()
        if date < today:
            messages.error(self.request, f"Event date must be in the future")
            return redirect("events:add")
        messages.success(
            self.request, f"You Created event {title} that will happen in {date}"
        )
        return super().form_valid(form)


@login_required
def AddParticipant(request, pk):
    """[summary]
    AddParticipant

    User can goto to Event
    User can Ignore Event

    url: addparticipant/<int:pk>/
    pk = event.id
    """

    event = get_object_or_404(Event, id=pk)
    participated = event.participants.filter(id=request.user.id)
    if event.done_event:
        messages.warning(
            request, f"Sorry, {event.title} is already take place in {event.date}"
        )
        return redirect("home")

    if participated:
        event.participants.remove(request.user)
        messages.warning(request, f"You withdrawed {event.title}")
    else:
        event.participants.add(request.user)
        messages.success(
            request, f"You are going to {event.title} that will happen in {event.date}"
        )
    return redirect("home")


@login_required
def EventUpdateView(request, pk):
    """[summary]
    EventUpdateView -> Event Update

    Update new Event

    url: /event/update/<int:pk>/
    pk = event.id
    """

    event = Event.objects.get(id=pk)
    if request.user != event.owner:
        return redirect("events:add")

    context = {}
    obj = get_object_or_404(Event, id=pk)
    form = EventForm(request.POST or None, instance=obj)
    if form.is_valid():
        date = form.cleaned_data["date"]
        today = datetime.date.today()
        if date < today:
            messages.error(request, f"Event date must be in the future")
            return redirect("events:update", pk=pk)
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    template_name = "pages/edit_event.html"
    messages.success(request, f"You Updated {event.title}")
    return render(request, template_name, context)


@login_required
def EventDeleteView(request, pk):
    """[summary]
    EventDeleteView -> Event Delete

    Update new Event

    url: /event/delete/<int:pk>/
    pk = event.id
    """

    event = Event.objects.get(id=pk)
    if request.user != event.owner:
        return redirect("events:add")

    context = {}  # type: ignore
    event = get_object_or_404(Event, id=pk)
    if request.method == "POST":
        event.delete()
        return HttpResponseRedirect("/")
    template_name = "pages/event_delete.html"
    messages.warning(request, f"You Going to Deleted {event.title}")
    return render(request, template_name, context)