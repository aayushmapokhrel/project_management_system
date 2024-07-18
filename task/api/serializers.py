from rest_framework import serializers
from task.models import Task
from project.models import Project
from task.models import Sprint
from employee.models import Employee
from rest_framework.validators import ValidationError
from datetime import datetime


class TaskSerializers(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    sprint = serializers.PrimaryKeyRelatedField(
        queryset=Sprint.objects.all(), many=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), many=True
    )
    type = serializers.IntegerField(required=True)

    class Meta:
        model = Task
        exclude = ["created_by", "modified_by"]
        
    def validate_type(self, type):
        task_type = set((i.value) for i in Task.Tasktype)
        if type not in task_type:
            raise ValidationError("Invalid Type")
        return type
    def validate_due_date(self, due_date):
        print(due_date, datetime.now().date())
        if due_date<datetime.now().date():
            raise ValidationError("Due Date should not beyond today date")
        
        return due_date
            
            
class SprintSerializers(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Sprint
        exclude = ["modified_by"]


class ReadSprintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ["name", "point", "created_by"]
