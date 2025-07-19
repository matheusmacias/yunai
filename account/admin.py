from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin interface for the custom user model.
    """

    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Informações pessoais", {"fields": ("first_name", "last_name")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

    list_per_page = 20
    search_help_text = "Digite o nome ou e-mail do usuário para pesquisar."

    def get_search_results(self, request, queryset, search_term):
        """
        Custom search method to filter users by email or username.
        """
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term
        )
        if search_term:
            queryset |= self.model.objects.filter(email__icontains=search_term)
            queryset |= self.model.objects.filter(username__icontains=search_term)
        return queryset, use_distinct


# Register ContentType admin to enable autocomplete
@admin.register(ContentType)
class CustomContentTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "app_label", "model")
    list_filter = ("app_label",)
    search_fields = ("name", "app_label", "model")
    ordering = ("app_label", "model")


@admin.register(Permission)
class CustomPermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "content_type")
    list_filter = ("content_type",)
    search_fields = ("name", "codename", "content_type__model")
    ordering = ("content_type__app_label", "content_type__model", "codename")
    autocomplete_fields = ["content_type"]
    list_per_page = 20
    search_help_text = "Busque por nome, codename ou modelo relacionado."
