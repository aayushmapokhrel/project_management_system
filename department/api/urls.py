from django.urls import path
from department.api.views import (
    DepartmentAPIView,
    DepartMentUpdateView,
    DesignationAPIVIEW,
    DesignationUpdateView,
)

urlpatterns = [
    path("", DepartmentAPIView.as_view(), name="department-view"),
    path("<int:pk>", DepartMentUpdateView.as_view(), name="department-update"),
    path("designation", DesignationAPIVIEW.as_view(), name="designation-view"),
    path(
        "designation/<int:id>",
        DesignationUpdateView.as_view(),
        name="designation-update",
    ),
]
