from django.urls import path,include
from department.api.views import department_list, create_department
urlpatterns = [
    
    path('',department_list, name="department"),
    path('create',create_department, name="department")

]
