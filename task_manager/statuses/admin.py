from django.contrib import admin

# Register your models here.
from .models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fileds = ["name",]
    list_display = (
        "name",
        "created_at"
    )
