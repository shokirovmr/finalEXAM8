from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    ImageField,
    CharField,
    BooleanField
)

from apps.task1.managers import UserManager


class User(AbstractUser):
    avatar = ImageField(upload_to="user/%Y/%m/%d")
    email = None
    is_active = BooleanField(default=False)
    token = CharField(max_length=128)
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
    manager = UserManager()

    def str(self):
        return self.username
