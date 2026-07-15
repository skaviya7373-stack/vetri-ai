from django.contrib import admin
from .models import AIHistory


@admin.register(AIHistory)
class AIHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "topic",
        "feature",
        "created_at",
    )

    search_fields = (
        "topic",
        "feature",
    )

    list_filter = (
        "feature",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20