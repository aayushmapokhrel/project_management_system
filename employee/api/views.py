from rest_framework.response import Response
from employee.models import Employee
from employee.api.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from drf_spectacular.utils import extend_schema


class EmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=EmployeeSerializer,
        responses={200: EmployeeSerializer},
    )
    def get(self, request):
        data = Employee.objects.filter(is_active=True)
        serializer = EmployeeSerializer(data, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=EmployeeSerializer,
        responses={200: EmployeeSerializer},
    )
    def post(self, request):
        data = request.data
        serialzier = EmployeeSerializer(data=data)
        if serialzier.is_valid():
            employee = serialzier.save()
            employee.created_by = request.user
            employee.save()
            return Response(
                {
                    "message": "Data successfully added",
                    "data": serialzier.data
                    },
                status=status.HTTP_200_OK,
            )
        return Response(
            serialzier.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class EmployeeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=EmployeeSerializer,
        responses={200: EmployeeSerializer},
    )
    def put(self, request, pk):
        qs = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(data=request.data, instance=qs)
        if serializer.is_valid():
            employee = serializer.save()
            # employee.modified_by = request.user
            employee.save()
            return Response(
                {
                    "message": "Data successfully updated",
                    "data": serializer.data
                    },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def delete(self, request, pk):
        qs = Employee.objects.get(id=pk)
        if qs.created_by.id != request.user.id:
            return Response(
                {
                    "error": f"Only created user can delete {qs.name} employee"
                    },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        qs.delete()
        return Response(
            {
                "message": "Data successfully deleted",
            },
            status=status.HTTP_200_OK,
        )
