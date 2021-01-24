from .models import User
from django.contrib.auth import forms as auth_forms


class UserChangeForm(auth_forms.UserChangeForm):
    """[summary]
    UserChangeForm -> User Update

    User update his data
    """

    class Meta:
        model = User
        fields = "__all__"


class UserCreationForm(auth_forms.UserCreationForm):
    """[summary]
    UserCreationForm -> User Create

    Create user account
    """

    class Meta:
        model = User
        fields = ("email",)