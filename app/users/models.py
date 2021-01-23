from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.urls import reverse


class UserManager(BaseUserManager):
    # pylint: disable=arguments-differ
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return super().create_user("", email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return super().create_superuser("", email, password, **extra_fields)


class User(AbstractUser):

    username = None  # type: ignore
    email = models.EmailField("Email", blank=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["email"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    @property
    def is_email_verified(self):
        return self.emailaddress_set.filter(email=self.email, verified=True).exists()