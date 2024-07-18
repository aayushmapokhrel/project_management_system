from rest_framework import serializers
from employee.models import Employee
from department.models import Designation


class EmployeeSerializer(serializers.ModelSerializer):
    designation = serializers.PrimaryKeyRelatedField(
        queryset=Designation.objects.all()
        )
    email = serializers.EmailField()
    phone = serializers.IntegerField()
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    class Meta:
        model = Employee
        exclude = ["created_by", "modified_by"]
    
    def validate_email(self, value):
        if Employee.objects.filter(email=value):
            raise serializers.ValidationError(
                "An employee with this email already exists."
            )
        return value

    def validate_phone(self, value):
        if Employee.objects.filter(phone=value):
            raise serializers.ValidationError(
                "An employee with this phone number already exists."
            )
        return value


class ReadEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name','address','employee_id','designation']

    def to_representation(self, instance):
        data= super().to_representation(instance)
        designation = Designation.objects.get(id=data['designation'])
        data.pop('designation')
        data['designation_name'] = designation.name
        data['department_name'] = designation.department.name
        return data
    
    
