"""Admin for courses app."""

from django.contrib import admin
from .models import Teacher, ScheduleChange


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'code',
        'created_at',
        'updated_at',
    ]


@admin.register(ScheduleChange)
class ScheduleAdmin(admin.ModelAdmin):
    pass
