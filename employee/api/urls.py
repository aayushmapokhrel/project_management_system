from django.urls import path
from employee.api.views import EmployeeAPIView, EmployeeUpdateView

urlpatterns = [
    path("", EmployeeAPIView.as_view(), name="employee-view"),
    path("<int:pk>", EmployeeUpdateView.as_view(), name="employee-update"),
]
