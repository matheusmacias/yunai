from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    first_name = models.CharField(max_length=150, verbose_name="Nome")
    last_name = models.CharField(max_length=150, verbose_name="Sobrenome")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    full_name = models.CharField("Nome Completo", max_length=150)
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Avatar"
    )
    is_verified = models.BooleanField(default=False, verbose_name="E-mail verificado")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.email
