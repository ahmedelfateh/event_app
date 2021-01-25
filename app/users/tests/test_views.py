import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from app.users.models import User
from app.users.tests.factories import UserFactory
from app.users.views import (
    UserRedirectView,
    UserUpdateView,
    user_detail_view,
)


@pytest.mark.django_db
class TestUserUpdateView:
    def test_get_success_url(self, user: User, rf: RequestFactory):
        """[summary]
        Test UserUpdateView return the correct /users/{user.id}/ (user detail)
        """

        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.id}/"

    def test_get_object(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


@pytest.mark.django_db
class TestUserRedirectView:
    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.id}/"


@pytest.mark.django_db
class TestUserDetailView:
    def test_authenticated(self, user: User, rf: RequestFactory):
        """[summary]
        Test Login user can see /users/{user.id}/ (user detail)
        """

        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = user_detail_view(request, pk=user.id)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        """[summary]
        Test anonymous user can see /users/{user.id}/ (user detail)
        """

        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = user_detail_view(request, pk=user.id)

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/fake-url/"
