from rest_framework import serializers
from department.models import Department

class DepartMentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'