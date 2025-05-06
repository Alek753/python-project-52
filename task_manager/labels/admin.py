from django.contrib import admin

# Register your models here.
from .models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    search_fileds = ["name",]
    list_display = (
        "name",
        "created_at"
    )
