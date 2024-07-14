from django.contrib import admin
from task.models import Task, TaskComment, Sprint

# Register your models here.
@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display= ['project', 'name', 'due_date']
    search_fields = ['project', 'name']

@admin.register(TaskComment)
class TaskcommentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'comment']
    search_fields = ['employee']

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    search_fields = ['name']