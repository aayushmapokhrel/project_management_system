from django.urls import path
from department.api.views import  DepartmentAPIView, DepartMentUpdateView

urlpatterns = [    
    path('',DepartmentAPIView.as_view(),name="department-view"),
    path('<int:pk>',DepartMentUpdateView.as_view(),name="department-update")

]
