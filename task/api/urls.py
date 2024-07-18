from django.urls import path
from task.api.views import(
            TaskAPIView,
            TaskUpdateView,
            SprintAPIView,
            SprintUpdateView
)

urlpatterns = [
    path('', TaskAPIView.as_view(), name='task_view'),
    path('<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('sprint/', SprintAPIView.as_view(), name='sprint_view'),
    path('sprint/<int:pk>', SprintUpdateView.as_view(), name='task_update'),


]