from rest_framework import serializers
from department.models import Department, Designation


class DepartMentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Department
        exclude = ["created_by", "modified_by"]


class DesignationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    department = DepartMentSerializer()

    class Meta:
        model = Designation
        exclude = ["created_by", "modified_by"]
