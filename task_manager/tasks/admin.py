from django.contrib import admin

# Register your models here.
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fileds = ["name",]
    list_display = (
        "id",
        "name",
        "status",
        "executor",
        "created_at"
    )
    list_filter = (
        "status",
        "executor"
    )
