from rest_framework.response import Response
from rest_framework.decorators import api_view
from department.models import Department
from department.api.serializers import DepartMentSerializer

@api_view(['GET'])
def department_list(request):
    data = Department.objects.filter(is_active=True)
    serializer = DepartMentSerializer(data, many=True) 
    return Response(serializer.data)
    
@api_view(['POST'])
def create_department(request):
    data = request.data
    serialzier = DepartMentSerializer(data=data)
    if serialzier.is_valid():
        serialzier.save()
        return Response({
            "message":"Data successfully added"
        })
    return Response(serialzier.errors)