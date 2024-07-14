from rest_framework.response import Response
from department.models import Department
from department.api.serializers import DepartMentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import status


class DepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Department.objects.filter(is_active=True)
        serializer = DepartMentSerializer(data, many=True) 
        return Response(serializer.data)
    
    
    def post(self,request):
        data = request.data
        data['created_by']=request.user.id
        data['modified_by']=request.user.id
        serialzier = DepartMentSerializer(data=data)
        if serialzier.is_valid():
            serialzier.save()
            return Response({
                "message":"Data successfully added",
                "data":serialzier.data
            },status=status.HTTP_200_OK)
        return Response(serialzier.errors,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    