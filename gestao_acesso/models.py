from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email é obrigatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, default="teste@exemplo.com")
    is_active = models.BooleanField(default=True)  # Recomendável adicionar
    is_staff = models.BooleanField(default=False)  # Necessário para admin
    is_superuser = models.BooleanField(default=False)
    cardId = models.CharField(max_length=100, unique=True, null=True)

    objects = UsuarioManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# Create your models here.
class LogAcess(models.Model):
    class Meta:
        ordering = ["-timestamp"]

    card_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    

