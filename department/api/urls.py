from django.urls import path
from department.api.views import  DepartmentAPIView

urlpatterns = [    
    path('',DepartmentAPIView.as_view(),name="department-view")
]
