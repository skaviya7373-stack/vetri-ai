from django.db import models
from django.contrib.auth.models import User


class AIHistory(models.Model):

    FEATURE_CHOICES = [
        ("Notes", "Notes"),
        ("Quiz", "Quiz"),
        ("Flashcards", "Flashcards"),
        ("Study Plan", "Study Plan"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ai_history"
    )

    topic = models.CharField(
        max_length=200
    )

    feature = models.CharField(
        max_length=20,
        choices=FEATURE_CHOICES
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "AI History"
        verbose_name_plural = "AI Histories"

    def __str__(self):
        return f"{self.user.username} - {self.topic} ({self.feature})"