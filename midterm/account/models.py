from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserProfileManager
from .utils import USER_ROLES, USER_ROLE_QUEST


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_ROLE_QUEST)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
