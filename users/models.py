"""Models for the user app."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Teacher


class User(AbstractUser):

    """User model."""

    courses = models.ManyToManyField(
        to=Teacher,
        blank=True,
        related_name='courses_set'
    )

    is_subscribing = models.BooleanField(
        default=False,
        null=False,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name or self.last_name else self.username
