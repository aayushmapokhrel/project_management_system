from rest_framework.response import Response
from task.models import Task, Sprint, TaskComment
from task.api.serializers import TaskSerializers, SprintSerializers, ReadSprintSerializers, TaskCommentSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
<<<<<<< HEAD
from rest_framework import status, generics
=======
from rest_framework import status
from rest_framework.generics import GenericAPIView
from project.models import Project
from django.db.models import Count
>>>>>>> b041b8d (Perform statistics on task)


class TaskAPIView(APIView):
  permission_classes = [IsAuthenticated]
  
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )
  
  def get(self, request):
    data = Task.objects.all()
    serializer = TaskSerializers(data, many=True)
    return Response(serializer.data)
  
  @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )

  def post(self, request):
        data = request.data
        serializer = TaskSerializers(data=data)
        if serializer.is_valid():
            task = serializer.save()
            task.save()
            return Response(
                {'message': 'Task successfully added', 'data': serializer.data},
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
                {
                    'error': f'Only Authorized can delete {query.name} Task'
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        query.delete()
        return Response(
            {
                'message': 'Task successfully deleted',
            },
            status=status.HTTP_200_OK,
        )
        

class SprintAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        request=ReadSprintSerializers,
        responses={200: SprintSerializers},
    )
    def get(self,request):
        data = Sprint.objects.all()
        serializer = ReadSprintSerializers(data, many=True)
        return Response(serializer.data)
    @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )
    def post(self, request):
        data = request.data
        serializer = SprintSerializers(data=data)
        if serializer.is_valid():
            sprint = serializer.save()
            sprint.save()
            return Response(
            {
                'message': 'sprint successfully added', 'data': serializer.data
            },
            status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SprintUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        request=SprintSerializers,
        responses={200: SprintSerializers},
    )
    def put(self, request, pk):
        info = Sprint.objects.get(id=pk)
        serializer = SprintSerializers(data=request.data, instance=info)
        if serializer.is_valid():
            task = serializer.save()
            task.save()
            return Response(
                {
                    "message": "Sprint successfully updated", "data": serializer.data
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    
    @extend_schema(
        request=TaskSerializers,
        responses={200: TaskSerializers},
    )
   
    def delete(self, request, pk):
        query = Sprint.objects.get(id=pk)
        if query.created_by.id != request.user.id:
            return Response(
                {
                    'error': f'Only Authorized can delete {query.name} Sprint'
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        query.delete()
        return Response(
            {
                'message': 'Sprintsuccessfully deleted',
            },
            status=status.HTTP_200_OK,
        )
        
class TaskCommentCreateAPIView(generics.ListCreateAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializers
  

class TaskCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializers
    

# for taskstats

class TaskStats(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        total_tasks = Task.objects.filter(project_id=id).count()
        task_counts = Task.objects.filter(project_id=id).values('status').annotate(count=Count('status')).order_by('status')
        status_dict = dict(Task.Taskstatus.choices)  # Convert choices to a dict
        status_counts = {
            status_dict.get(data['status']):data['count'] 
            for data in task_counts
            }
        
        result = {
            'Totaltasks': total_tasks,
            'Status_count': status_counts
        }

        return Response(result, status=status.HTTP_200_OK)
