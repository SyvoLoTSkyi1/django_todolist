from django.contrib import admin

from tasks.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'complete')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
