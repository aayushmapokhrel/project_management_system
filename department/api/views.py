from rest_framework.response import Response
from department.models import Department, Designation
from department.api.serializers import DepartMentSerializer, DesignationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class DepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Department.objects.filter(is_active=True)
        serializer = DepartMentSerializer(data, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=DepartMentSerializer,
        responses={200: DepartMentSerializer},
    )
    def post(self, request):
        data = request.data
        serialzier = DepartMentSerializer(data=data)
        if serialzier.is_valid():
            department = serialzier.save()
            department.created_by = request.user
            department.save()
            return Response(
                {"message": "Data successfully added", "data": serialzier.data},
                status=status.HTTP_200_OK,
            )
        return Response(serialzier.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DepartMentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        qs = Department.objects.get(id=pk)
        serializer = DepartMentSerializer(data=request.data, instance=qs)
        if serializer.is_valid():
            department = serializer.save()
            department.modified_by = request.user
            department.save()
            return Response(
                {"message": "Data successfully updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        qs = Department.objects.get(id=pk)
        if qs.created_by.id != request.user.id:
            return Response(
                {"error": f"Only created user can delete {qs.name} department"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        qs.delete()
        return Response(
            {
                "message": "Data successfully deleted",
            },
            status=status.HTTP_200_OK,
        )


class DesignationAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Designation.objects.filter(is_active=True)
        serializer = DesignationSerializer(data, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=DesignationSerializer,
        responses={200: DesignationSerializer},
    )
    def post(self, request):
        data = request.data
        serialzier = DesignationSerializer(data=data)
        if serialzier.is_valid():
            designation = serialzier.save()
            designation.created_by = request.user
            designation.save()
            return Response(
                {"message": "Data successfully added", "data": serialzier.data},
                status=status.HTTP_200_OK,
            )
        return Response(serialzier.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DesignationUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        qs = Designation.objects.get(id=id)
        serializer = DesignationSerializer(data=request.data, instance=qs)
        if serializer.is_valid():
            designation = serializer.save()
            designation.modified_by = request.user
            designation.save()
            return Response(
                {"message": "Data successfully updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, id):
        qs = Designation.objects.get(id=id)
        if qs.created_by.id != request.user.id:
            return Response(
                {"error": f"Only created user can delete {qs.name} designation"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        qs.delete()
        return Response(
            {
                "message": "Data successfully deleted",
            },
            status=status.HTTP_200_OK,
        )
