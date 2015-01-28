from django.contrib import admin
from models import Task


class TaskAdmin(admin.ModelAdmin):
   fieldsets = [
        ('Task',               {'fields': ['title', 'completed']}),
        ('Information', {'fields': ['assignedby', 'assignedto', 'assigned_date', 'due_date','description']}),
    ]


# Register your models here.
admin.site.register(Task, TaskAdmin) 