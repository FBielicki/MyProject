"""Models for teachers app."""

from django.db import models

from courses.choices import ScheduleChangeTypeChoices, Grades
from utils.models import BaseModel


class Teacher(BaseModel):

    """Teacher model."""

    first_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=64,
        blank=False,
        null=True
    )

    code = models.CharField(
        unique=True,
        max_length=64,
        blank=True,
        null=False
    )

    def __str__(self):
        return f'Teacher: {self.last_name} {self.code.capitalize()}'


class ScheduleChange(BaseModel):

    """Schedule change model."""

    teacher = models.ForeignKey(
        Teacher,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    type = models.CharField(null=True, max_length=64)

    date = models.DateField()

    absent_from = models.IntegerField(null=True)

    absent_to = models.IntegerField(null=True)

    new_classroom = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )

    new_teacher = models.ForeignKey(
        Teacher,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='substitutes'
    )

    course = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )

    degree = models.CharField(
        null=True,
        blank=True,
        max_length=16
    )

    additional_text = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.absent_from} - {self.absent_to} | {self.teacher.code} {str(self.type)}'


class Class(BaseModel):

    """Class model"""

    code = models.CharField(max_length=16, null=False, blank=False)

    url_param = models.CharField(max_length=16, null=False, blank=False)
