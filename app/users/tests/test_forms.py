import pytest
from app.users.tests.factories import UserFactory
from app.users.forms import UserCreationForm


@pytest.mark.django_db
class TestUserCreationForm:
    def test_clean_email(self):
        """[summary]
        Test user create form
        """

        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserCreationForm(
            {
                "email": proto_user.email,
                "password1": proto_user.password,
                "password2": proto_user.password,
            }
        )

        assert form.is_valid()

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "email": proto_user.email,
                "password1": proto_user.password,
                "password2": proto_user.password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "email" in form.errors
