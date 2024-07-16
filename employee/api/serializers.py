from rest_framework import serializers
from employee.models import Employee
from department.models import Designation


class EmployeeSerializer(serializers.ModelSerializer):
    designation = serializers.PrimaryKeyRelatedField(
        queryset=Designation.objects.all()
        )

    class Meta:
        model = Employee
        exclude = ["created_by", "modified_by"]
