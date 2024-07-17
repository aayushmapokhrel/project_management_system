from rest_framework import serializers
from task.models import Task
from project.models import Project
from task.models import Sprint
from employee.models import Employee

from employee.api.serializers import ReadEmployeeSerializer


class TaskSerializers(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
		queryset=Project.objects.all()
    )
    sprint = serializers.PrimaryKeyRelatedField(
        queryset=Sprint.objects.all(),
        many=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        many=True
    )

    class Meta:
        model = Task
        exclude = ["created_by", "modified_by"]


class TaskGetSerializers(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
		queryset=Project.objects.all()
    )
    sprint = serializers.PrimaryKeyRelatedField(
        queryset=Sprint.objects.all(),
        many=True
    )
    assigned_to = serializers.ListSerializer(
        child=ReadEmployeeSerializer(required=True),
        required=False
    )
    class Meta:
         model = Task
         exclude = ["created_by", "modified_by"]
    