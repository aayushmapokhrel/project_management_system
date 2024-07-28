from django.urls import path
from task.api.views import (
    TaskAPIView,
    TaskUpdateView,
    SprintAPIView,
    SprintUpdateView,
    TaskCommentCreateAPIView,
    TaskCommentRetrieveUpdateDestroyAPIView,
    TaskStats,
    taskboard
)

urlpatterns = [
    path("", TaskAPIView.as_view(), name="task_view"),
    path("<int:pk>", TaskUpdateView.as_view(), name="task_update"),
    path("sprint/", SprintAPIView.as_view(), name="sprint_view"),
    path("sprint/<int:pk>", SprintUpdateView.as_view(), name="task_update"),
    path("comment/", TaskCommentCreateAPIView.as_view(), name="comment_create_list"),
    path(
        "comment_rud/<int:pk>/",
        TaskCommentRetrieveUpdateDestroyAPIView.as_view(),
        name="comment_create_list",
    ),
    path("stats/<int:id>/", TaskStats.as_view(), name="task-stats"),
    path('board', taskboard,name="task-broard")
]
