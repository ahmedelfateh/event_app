import pytest
from django.urls import resolve, reverse

from app.users.models import User


@pytest.mark.django_db
def test_detail(user: User):
    assert reverse("users:detail", kwargs={"pk": user.pk}) == f"/users/{user.id}/"
    assert resolve(f"/users/{user.id}/").view_name == "users:detail"


@pytest.mark.django_db
def test_update():
    assert reverse("users:update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:update"


@pytest.mark.django_db
def test_redirect():
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect"
