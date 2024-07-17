from django.urls import path
from task.api.views import(
            TaskAPIView,
            TaskUpdateView,
)

urlpatterns = [
    path('', TaskAPIView.as_view(), name='task_view'),
    path('<int:pk>', TaskUpdateView.as_view(), name='task_update'),


]