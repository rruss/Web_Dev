from django.contrib import admin
from .models import TaskList, Task
# Register your models here.
# admin.site.register(TaskList)

admin.site.register(Task)


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')
