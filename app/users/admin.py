from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from allauth.account.models import EmailAddress
from .models import User
from .forms import UserChangeForm, UserCreationForm


class EmailsInline(admin.TabularInline):
    model = EmailAddress
    readonly_fields = ["user"]
    max_num = 8
    extra = 0


admin.site.unregister(EmailAddress)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (
            "Personal info",
            {"fields": ("email",)},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    # "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "is_staff",
    )
    search_fields = ["email"]
    ordering = ("email",)
    list_display_links = ["email"]
    inlines = [EmailsInline]
