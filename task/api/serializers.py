from rest_framework import serializers
from task.models import Task
from project.models import Project
from task.models import Sprint
from employee.models import Employee


class TaskSerializers(serializers.ModelSerializer):
  project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
  sprint = serializers.PrimaryKeyRelatedField(queryset=Sprint.objects.all(), many=True)
  assigned_to = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)
  class Meta:
    model = Task
    exclude = ["created_by", "modified_by"] 

class SprintSerializers(serializers.ModelSerializer):
  created_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
  class Meta:
    model = Sprint
    exclude = ["modified_by"]
    
class ReadSprintSerializers(serializers.ModelSerializer):
  class Meta:
    model = Sprint
    fields = ["name","point","created_by"]