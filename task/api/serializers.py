from rest_framework import serializers
from task.models import Task
from project.models import Project
from task.models import Sprint
from task.models import TaskComment
from employee.models import Employee
from rest_framework.validators import ValidationError
from datetime import datetime
from django.db.models import Sum


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
        fields = '__all__'
        # exclude = ["created_by", "modified_by"]
    
    def validate(self, data):
        task_points = Task.objects.filter(sprint=data['sprint'][0].id).aggregate(count = Sum('points'))
        if task_points['count'] is None:
            total_task_point = 0
        else:
            total_task_point = data.get('points')+task_points["count"]
        if data['sprint'][0].point < total_task_point:
            raise ValidationError("Overall task point is greater than sprint  point")
        return data
    
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

class TaskCommentSerializers(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(),required=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),required=True)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),required=True)
    comment = serializers.CharField(required=True)
    class Meta:
        model = TaskComment  
        fields='__all__'
        read_only_fields = ["modified_by", "file","modified_at", "created_at", "employee"]
    

class TaskGetSerializers(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    sprint = serializers.PrimaryKeyRelatedField(
        queryset=Sprint.objects.all(), many=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), many=True
    )
    type = serializers.IntegerField(required=True)
    task_comment = TaskCommentSerializers(many=True)

    class Meta:
        model = Task
        fields = '__all__'    