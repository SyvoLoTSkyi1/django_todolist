from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=155,
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'tasks.Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True

    )
    complete = models.BooleanField(
        default=False
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class Category(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
