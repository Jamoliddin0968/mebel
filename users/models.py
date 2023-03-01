from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

OLINDI = "Olindi"
BERILDI = "Berildi"
OLINDI_KOEFFITSIYENT = -1
BERILDI_KOEFFITSIYENT = 1

MANAGE_TYPES = (
    (OLINDI_KOEFFITSIYENT, OLINDI),
    (BERILDI_KOEFFITSIYENT, BERILDI)
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

# Worker


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            _("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Bu username bazada mavjud"),
        },
    )
    name = models.CharField(max_length=255, verbose_name="F.I.Sh")
    phone = models.CharField(
        max_length=255, verbose_name=_("Telefon raqami"), null=True)
    address = models.CharField(
        max_length=255, verbose_name=_("Manzili"), null=True)
    birth_date = models.DateField(verbose_name=_("Tug'ilgan kuni"), null=True)
    salary = models.PositiveIntegerField(default=0)
    percentage = models.PositiveIntegerField(default=0)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.name
    class Meta:
        # managed=False
        verbose_name = _("Hodim")
        verbose_name_plural = _("Hodimlar")
        db_table = "users"


class AllowedUsers(models.Model):
    user = models.ForeignKey('users.User', models.DO_NOTHING,
                             blank=True, null=True, verbose_name=_("Hodim"))
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = _("Ruxsat berilgan")
        verbose_name_plural = _("Ruxsat berilganlar")
        db_table = 'allowed_users'

# Xaridor


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Xaridor"))
    phone = models.CharField(max_length=255, verbose_name=_("Telefon raqam"))
    address = models.CharField(max_length=255, verbose_name=_("Manzil"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Xaridor")
        verbose_name_plural = _("Xaridorlar")
        db_table = 'customer'


# Jarimalar


class Penalty(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING,
                             verbose_name=_("Hodim"))
    cash = models.IntegerField(default=0, verbose_name=_("Pul miqdori"))
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Jarima")
        verbose_name_plural = _("Jarimalar")
        db_table = 'penalty'


# Ta'minotchilar


class Provider(models.Model):
    name = models.CharField(verbose_name=_("F.I.SH"), max_length=255)
    corporation = models.CharField(
        verbose_name=_("Corporation"), max_length=255)
    address = models.CharField(verbose_name=_("Manzili"), max_length=255)
    phone = models.CharField(verbose_name=_("Telefon raqami"), max_length=255)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = _("Ta'minotchi")
        verbose_name_plural = _("Ta'minotchilar")
        db_table = 'provider'

# Ta'minotchi bilan hiosb-kitob


class ProviderManagement(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING,
                             verbose_name=_("Hodim"))
    provider = models.ForeignKey(
        Provider, models.DO_NOTHING, verbose_name=_("Ta'minotchi"))
    cash = models.IntegerField(verbose_name=_("Pul miqdori"))
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.provider.name 
    class Meta:
        verbose_name = _("Ta'minotchi bilan hiosb-kitob")
        verbose_name_plural = _("Ta'minotchi bilan hiosb-kitob")
        db_table = 'provider_management'

