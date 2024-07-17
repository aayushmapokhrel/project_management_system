from rest_framework.response import Response
from task.models import Task
from task.api.serializers import TaskSerializers,TaskGetSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import status


class TaskAPIView(APIView):
  permission_classes = [IsAuthenticated]
  
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskGetSerializers},
    )
  
  def get(self, request):
    data = Task.objects.all()
    serializer = TaskGetSerializers(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )

  def post(self, request):
        data = request.data
        serializer = TaskSerializers(data=data)
        print(type(data['assigned_to']))
        if serializer.is_valid():
            task = serializer.save()
            task.created_by_id = data['assigned_to'][0]
            task.save()
            return Response(
                {
                    'message': 'Task successfully added',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    
class TaskUpdateView(APIView):
  permission_classes = [IsAuthenticated]
  
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )

  def put(self, request, pk):
        info = Task.objects.get(id=pk)
        serializer = TaskSerializers(data=request.data, instance=info)
        if serializer.is_valid():
            task = serializer.save()
            task.save()
            return Response(
                {"message": "Task successfully updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )
   
  def delete(self, request, pk):
        query = Task.objects.get(id=pk)
        if query.created_by.id != request.user.id:
            return Response(
                {'error': f'Only Authorized can delete {query.name} Task'},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        query.delete()
        return Response(
            {
                'message': 'Task successfully deleted',
            },
            status=status.HTTP_200_OK,
        )