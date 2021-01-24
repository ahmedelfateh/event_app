from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    """[summary]
    UserDetailView -> User Profile

    User view his data

    url: /users/<int:pk>/
    pk = user.id
    """

    model = User


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    """[summary]
    UserUpdateView -> User update

    User update his data

    url: /users/~update/
    """

    model = User
    fields = [
        "email",
    ]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.id})

    def get_object(self):
        return User.objects.get(id=self.request.user.id)  # type: ignore

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    """[summary]
    url: /users/~update/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.id})


user_redirect_view = UserRedirectView.as_view()
