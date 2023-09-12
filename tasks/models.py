from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=155,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'tasks.Category',
        on_delete=models.CASCADE,

    )
    complete = models.BooleanField(
        default=False
    )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
