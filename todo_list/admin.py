from django.contrib import admin

from todo_list.models import Task, Tags


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("tags",)
    list_filter = ("tags",)


admin.site.register(Tags)
