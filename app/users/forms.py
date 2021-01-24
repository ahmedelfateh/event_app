from .models import User
from django.contrib.auth import forms as auth_forms


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")